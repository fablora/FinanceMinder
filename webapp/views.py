import logging
from  .filters import ExpenseFilter
from .forms import AddCategoryForm, AddExpenseForm, AddIncomeForm
from .models import Category, Currency, Expense
from .tables import ExpenseHTMxTable

from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django_filters.views import FilterView
from django_tables2 import SingleTableMixin

# Get logger instance
logger = logging.getLogger(__name__)

# Request for Index page
def index(request):
    """
    Handle the creation of a new expense via the AddExpenseForm.
    """
    expense_form = AddExpenseForm(request.POST or None)
    income_form = AddIncomeForm(request.POST or None)

    if request.method == "POST":
        if 'expense' in request.POST:
            if expense_form.is_valid():
                new_expense = expense_form.save()
                messages.success(request, "Expense Added Successfully")
                return redirect('index')
            else:
                messages.error(request, "Please correct the errors below.")
        elif 'income' in request.POST:
            if income_form.is_valid():
                new_income = income_form.save()
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

# Request for responsive bar chart        
def barDashboard(request):
    """View to render dashboard with Dash app."""
    return render(request, "bar_chart.html")

# Request for responsive pie chart
def pieDashboard(request):
    """View to render dashboard with Dash app."""
    return render(request, "pie_chart.html")

