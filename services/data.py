from webapp.models import Expense, Income
from django.db.models import Sum
from django.db.models.functions import ExtractMonth, ExtractYear

from datetime import datetime
import pandas as pd
import numpy as np
from functools import lru_cache 
from .files import cached_download_cpi

    
# Function to get filtered expenses
def get_filtered_expenses(start_date=None, end_date=None):
    '''
    Retrieve filtered expenses within specified date range

    Parameters:
    start_date (str): Start date for the filter
    end_date (str): End date for the filter

    Returns:
    QuerySet: Filtered expenses
    '''
   
    expenses = Expense.objects.all()
    if start_date:
        expenses = expenses.filter(date__gte=start_date)
    if end_date:
       expenses = expenses.filter(date__lte=end_date)
   
    return expenses

# Function to aggregate expense data by Category
def get_category_expense_data(start_date=None, end_date=None):
    '''
    Get agreggated expense data by category within the specified date range

    Parameters:
    start_date (str): Start date for the filter
    end_date (str): End date for the filter

    Returns:
    tuple: Categories, amount and percentage of total expenses
    '''
    try:
        expenses = get_filtered_expenses(start_date, end_date)
        data = expenses.values('category__name').annotate(total_sum=Sum('amount')).order_by('-total_sum')
        total_expenses = sum(item['total_sum'] for item in data)
        categories = [item['category__name'] for item in data]
        amounts = [item['total_sum'] for item in data]
        percentage = [(item['total_sum'] / total_expenses) * 100 for item in data]

        return categories, amounts, percentage
    
    except Exception as e:
       print(f"Error getting expense data: {e}")
       return [], [], []

# Function to get monthly expense by category
def get_monthly_expense_by_category(start_date=None, end_date=None):
    '''
    Get monthly expense data by category within specified date range

    Parameters:
    start_date (str): Start date for the filter
    end_date (str): End date for the filter

    Returns:
    DataFrame: Pivot table of monthly expenses by category
    '''
    try:
        expenses = get_filtered_expenses(start_date = None, end_date = None)

        data = list(expenses.values('date', 'amount', 'category__name'))
        df = pd.DataFrame(data)
        
        df.rename(columns={'category__name': 'category'}, inplace = True)

        df['date'] = pd.to_datetime(df['date'])
        df.set_index('date', inplace = True)

        monthly_expenses = df.groupby([pd.Grouper(freq = 'M'), 'category']).sum().reset_index()
        
        monthly_expenses_pivot = monthly_expenses.pivot(index = 'date', columns = 'category', values = 'amount')

        # Fill NA values with 0
        monthly_expenses_pivot =  monthly_expenses_pivot.fillna(0)

        return monthly_expenses_pivot
    
    except Exception as e:
       print(f"Error getting the expense data: {e}")


# Function to get latest CPI and the Salary CPI        
@lru_cache(None)
def get_cpis():
    '''
    Get the latest Consumer Price Index (CPI) and the CPI for the salary at the date 
    from the Australian Bureau of Statistics

    Returns:
    tuple: Latest CPI and the CPI for the salary at the date

    '''
    try:
        local_path = cached_download_cpi()
        excel_file = pd.ExcelFile(local_path)
        df = excel_file.parse("Data1")

        
        df.rename(columns={df.columns[0]: "Date"}, inplace=True)    # Rename the first column to "Date"
        df.index = df["Date"]

        
        column_name = "Index Numbers ;  All groups CPI ;  Australia ;"  # Defines series target
        cpi_series = df[column_name]

        # Get latest CPI    
        latest_cpi = cpi_series.tail(1).iloc[0]

        # Filter for salary CPI
        salary = Income.objects.filter(category__name='Salary').annotate(
            year = ExtractYear('date'),
            month = ExtractMonth('date')
        ).first()

        if not salary:
            raise ValueError("No salary entry found")
        
        # Formats salary's date for filtering purposes
        salary_date = datetime(year=salary.year, month=salary.month, day=1)

        # Defines salary's index
        salary_idx = np.searchsorted(cpi_series.index, salary_date, side = "right")-1

        salary_cpi = cpi_series.iloc[salary_idx]

        cpi_range = cpi_series.iloc[salary_idx:]
        

        return latest_cpi, salary_cpi, cpi_range, salary_date
    
    except Exception as e:
        print(f"Error getting CPI data: {e}")


# Function to calculate real salary
def calculate_real_salary():
   '''
   Calculate real salary adjusted for inflation

   Returns:
   tuple: Real salary, latest CPI, salary CPI, and salary inflation rate
   '''
   
   try:
        latest_cpi, salary_cpi, cpi_range, salary_date = get_cpis()

        if latest_cpi is None or salary_cpi is None:
            raise ValueError("CPI data not available")

        salary_entry = Income.objects.get(category__name='Salary')
        salary_amount = salary_entry.amount

        

        salary_inflation_rate = float((latest_cpi - salary_cpi) / salary_cpi * 100)
        real_salary = float(salary_amount) / (1 + (salary_inflation_rate / 100))

        real_salary = round(real_salary, 2)
        salary_inflation_rate = round(salary_inflation_rate, 2)
        
        return real_salary, latest_cpi, salary_cpi, salary_inflation_rate
   
   except Exception as e:
       print(f"Error calculating real salary: {e}")
       return None, None, None, None
  
def prepare_salary_trend_data():

    try:
        latest_cpi, salary_cpi, cpi_range, salary_date = get_cpis()
        if latest_cpi is None or salary_cpi is None:
            raise ValueError("CPI data not availbale")
        
        salary_entry =  Income.objects.get(category__name = 'Salary')
        salary_amount = salary_entry.amount

        trend_data = []

        for date, cpi in cpi_range.items():
            inflation_rate = float((cpi - salary_cpi) / salary_cpi * 100)
            adjusted_salary = float(salary_amount) / (1 + (inflation_rate / 100))
            trend_data.append((date, round(adjusted_salary, 2)))

        return trend_data
    
    except Exception as e:
        print(f"Error preparing salary trend data: {e}")
        return []      