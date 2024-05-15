from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div, Submit, ButtonHolder, Reset
from decimal import Decimal
from django.db.models import Q
from django_filters import NumberFilter, CharFilter, DateFromToRangeFilter
from django_filters.widgets import DateRangeWidget
from .models import *

import django_filters

class ExpenseFilter(django_filters.FilterSet):
    query = django_filters.CharFilter(method = 'universal_search', label = "Search")
    amount_from = NumberFilter(field_name = 'amount', lookup_expr = 'gte')
    amount_to = NumberFilter(field_name = 'amount', lookup_expr = 'lte')
    category = django_filters.ModelChoiceFilter(queryset=Category.objects.all())
    date_from_to = DateFromToRangeFilter(widget = DateRangeWidget(attrs={'type': 'date'}), field_name ='date')


    def __init__(self, *args, **kwargs):
        super(ExpenseFilter, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'get'
        self.helper.layout = Layout(
             Div(
                Field('query', css_class ='mb-2', wrapper_class ='col-sm', id ='query_filter_field'),
                Field('amount_from', css_class ='mb-2', wrapper_class ='col-sm', id ='amount_from_filter_field'),
                Field('amount_to', css_class ='mb-2', wrapper_class ='col-sm', id ='amount_to_filter_field'),
                Field('category', css_class ='mb-2', wrapper_class ='col-sm', id ='category_filter_field'),
                Field('date_from_to', css_class ='mb-2', wrapper_class ='col-sm', id ='date_range_filter_field', type ='date'),
                css_class='row g-2'  # Applies a consistent
            ),
            ButtonHolder(
                Submit('submit', 'Search', css_class ='btn btn-primary'),
                Reset('reset', 'Reset Filters', css_class ='btn btn-secondary', onclick ="setTimeout(() => { this.form.dispatchEvent(new Event('submit')); }, 10);")
            )
        )
        
    class Meta:
        model = Expense
        fields = ['query', 'amount_from','amount_to', 'category', 'date_from_to']

    def universal_search(self, queryset, name, value):
        try:
            # Attempt to convert the value to Decimal for amount comparison
            decimal_value = Decimal(value)
            amount_query = Q(amount=decimal_value)
        except Decimal.InvalidOperation:
            # If conversion fails, no amount query should be made
            amount_query = Q()

        # General text search across multiple fields
        text_query = Q(description__icontains=value) | \
                    Q(category__name__icontains=value) | \
                    Q(currency__code__icontains=value)

        # Combine both queries using OR (since amount might not always be relevant)
        # This ensures that amount queries are considered alongside text queries
        return queryset.filter(amount_query | text_query)