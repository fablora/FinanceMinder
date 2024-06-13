import django_tables2 as tables
from django.utils.html import format_html
from .models import *

# Responsive table for Expenses

class ExpenseHTMxTable(tables.Table):
    category = tables.Column(accessor ='category', verbose_name ='Category')
    date = tables.Column(accessor ='date', verbose_name ='Date')
    description = tables.Column(accessor ='description', verbose_name ='Description')
    amount = tables.Column(accessor ='amount', verbose_name ='Amount')
    currency = tables.Column(accessor ='currency.code', verbose_name ='Currency')


    class Meta:
        model = Expense
        template_name = "tables/bootstrap_htmx.html"
        fields = ('date', 'description', 'amount', 'currency')  # defines fields to display
        sequence = ('date', 'category', 'description', 'amount', 'currency')  # defines the order of the columns