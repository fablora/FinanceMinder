from .forms import AddCategoryForm, AddExpenseForm
from .models import Category, Currency, Expense
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect



# Request for index page
def index(request):
    """
    Handle the creation of a new expense via the AddExpenseForm.
    """
    form = AddExpenseForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            new_expense = form.save()
            messages.success(request, "Expense Added Successfully")
            return redirect('index')
        else:
            messages.error(request, "Please correct the errors below.")
    return render(request, 'index.html', {'form': form})