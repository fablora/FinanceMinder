import logging
import requests

from .filters import ExpenseFilter
from .forms import AddExpenseForm, AddIncomeForm
from .models import Expense, Income, IncomeCategory
from .tables import ExpenseHTMxTable
from services.data import calculate_real_salary, prepare_salary_trend_data

from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

# Get logger instance
logger = logging.getLogger(__name__)

# Request for Index page
def index(request):
    """
    Handles the creation of new expenses and incomes.
    """
    expense_form = AddExpenseForm(request.POST or None)
    income_form = AddIncomeForm(request.POST or None)

    salary_category = IncomeCategory.objects.get(name = 'Salary')

    if request.method == "POST":
        if 'add_expense' in request.POST:
            if expense_form.is_valid():
                new_expense = expense_form.save()
                messages.success(request, "Expense Added Successfully")
                return redirect('index')
            else:
                messages.error(request, "Please correct the errors below.")
        elif 'add_income' in request.POST:
            if income_form.is_valid():
                new_income = income_form.save(commit = False)
                if new_income.category == salary_category:
                    existing_salary = Income.objects.filter(category = salary_category).first()
                    if existing_salary:
                        messages.warning(request, "An existing salary will be replaced.")
                        existing_salary.delete()
                new_income.save()        
                messages.success(request, "Income Added Successfully")
                return redirect('index')
            else:
                messages.error(request, "Please correct the errors below.")
    return render(request, 'index.html', {'expense_form': expense_form, 'income_form': income_form})

# Request for responsive expense table
class ExpenseHTMxTableView(SingleTableMixin, FilterView):
    table_class = ExpenseHTMxTable
    queryset = Expense.objects.all()
    filterset_class = ExpenseFilter
    paginate_by = 20

    def get_template_names(self):
        if self.request.htmx:
            return ["expense_table_partial.html"]
        else:
            return ["expense_table_htmx.html"]
# Request for income page
def income_page(request):
    if request.is_ajax():

        real_salary_amount, latest_cpi, salary_cpi, salary_inflation_rate = calculate_real_salary()
        salary_trend_data = prepare_salary_trend_data()

        context = {
            'latest_cpi': latest_cpi,
            'salary_cpi': salary_cpi,
            'real_salary': real_salary_amount,
            'inflation_rate': salary_inflation_rate,
            'salary_trend_data': salary_trend_data
        }

        return JsonResponse(context)

    income = Income.objects.all()
    return render(request, "income_analysis.html", {'income' : income})

# Request for responsive bar chart        
def bar_dashboard(request):
    """View to render dashboard with Dash app."""
    return render(request, "bar_chart.html")

# Request for responsive pie chart
def pie_dashboard(request):
    """View to render dashboard with Dash app."""
    return render(request, "pie_chart.html")

# Request for responsive line chart
def line_dashboard(request):
    """View to render dashboard with Dash app."""
    return render(request, "expenses_line_chart.html")
