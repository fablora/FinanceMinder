from django import forms
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
from .models import Currency, Category, Expense

import datetime

# Add Currency Form

class AddCategoryForm(forms.ModelForm):
    """
    Form for creating a new category with validation to ensure the name contains only letters and spaces.

    Uses the Category model, includes all model fields in the form.
    The 'name' field uses a regex validator for alphabetical input and is styled with Bootstrap classes for UI consistency.
    """

    error_css_class = "error"

    name = forms.CharField(
        required = True,
        validators = [RegexValidator(regex = '^[a-zA-Z ]+$', message = 'The category name must contain only letters')], # Regex to validate only letters input
        widget = forms.widgets.TextInput(attrs = {"placeholder" : "Category Name", "class" : "form-control"}),
        label = "",
    )

    class Meta:
        model = Category
        exclude = ()

# Add Expense Form

class AddExpenseForm(forms.ModelForm):
    """
    Form for adding an expense, integrating specific fields: category, amount, currency, and date.

    Features:
    - Automatically sets the default currency to 'Australian Dollar' if available.
    - Uses HTML5 date picker for the date field with today's date as default.
    - Validators ensure descriptions are alphanumeric and amounts are numeric.
    - Styling with Bootstrap 'form-control' for consistent UI appearance.
    """
    
    error_css_class = "error"

    class Meta:
        model = Expense
        exclude = ()
        fields = ['amount', 'category' , 'currency', 'date', 'description']

    category = forms.ModelChoiceField(
        queryset = Category.objects.all(),
        to_field_name = 'name',
        required = True,
        widget = forms.Select(attrs = {'class' : 'form-control'})
    )

    amount = forms.DecimalField(
        required = True,
        widget = forms.widgets.TextInput(attrs = {"placeholder":"Amount", "class" : "form-control"}), 
        label = ""
    )

    currency = forms.ModelChoiceField(
        queryset = Currency.objects.all(),
        to_field_name = 'name',
        required = True,
        widget = forms.Select(attrs = {'class' : 'form-control'})
    )

    def __init__(self, *args, **kwargs):
        super(AddExpenseForm, self).__init__(*args, **kwargs)
        default_currency = Currency.objects.filter(name='Australian Dollar').first()
        if default_currency:
            self.fields['currency'].initial = default_currency.name    

    date = forms.DateField(
        required = True,
        widget=forms.DateInput(attrs = {
            'class' : 'form-control',
            'type' : 'date'  # Uses HTML5 date picker
        }),
        initial = datetime.date.today  # Sets today's date as default
    )

    description = forms.CharField(
        required = True,
        validators = [RegexValidator(regex = '^[A-Za-z0-9 ]+$', message = 'Description must contain only alphanumeric characters.')], 
        widget = forms.widgets.TextInput(attrs = {"placeholder":"Description", "class" : "form-control"}), 
        label = ""
        )
