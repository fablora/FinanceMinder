from webapp.models import Expense
from django.db.models import Sum

# Function to aggregate expense data by Category
def get_category_expense_data(start_date = None, end_date = None):
    expenses = Expense.objects.all()

    if start_date:
        expenses = expenses.filter(date__gte=start_date)
    if end_date:
        expenses = expenses.filter(date__lte=end_date)    

    data = expenses.values('category__name').annotate(total_sum = Sum('amount')).order_by('-total_sum')
    total_expenses = sum(item['total_sum'] for item in data)
    categories = [item['category__name'] for item in data]
    amounts = [item['total_sum'] for item in data]
    percentage = [(item['total_sum'] / total_expenses) * 100 for item in data]

    return categories, amounts, percentage