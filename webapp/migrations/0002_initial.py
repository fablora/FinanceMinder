import random
import django.db.models.deletion
from django.db import migrations, models
from datetime import date

def add_currency_data(apps, schema_editor):
    Currency = apps.get_model('webapp', 'Currency')
    currencies = [

        Currency(name = "United States Dollar", code = "USD", symbol = "$"),
        Currency(name= "Euro", code = "EUR", symbol = "€"),
        Currency(name = "Japanese Yen", code = "JPY", symbol = "¥"),
        Currency(name = "British Pound Sterling", code = "GBP", symbol = "£"),
        Currency(name = "Australian Dollar", code = "AUD", symbol = "$"),
        Currency(name = "Canadian Dollar", code = "CAD", symbol = "$"),
        Currency(name = "Swiss Franc", code = "CHF", symbol = "CHF"),
        Currency(name = "Chinese Yuan Renminbi", code = "CNY", symbol = "¥"),
        Currency(name = "Swedish Krona", code = "SEK", symbol = "kr"),
        Currency(name = "New Zealand Dollar", code = "NZD", symbol = "$"),
        Currency(name = "Mexican Peso", code = "MXN", symbol = "$"),
        Currency(name = "Singapore Dollar", code = "SGD", symbol = "$"),
        Currency(name = "Hong Kong Dollar", code = "HKD", symbol = "$"),
        Currency(name = "Norwegian Krone", code = "NOK", symbol = "kr"),
        Currency(name = "South Korean Won", code = "KRW", symbol = "₩"),
        Currency(name = "Turkish Lira", code = "TRY", symbol = "₺"),
        Currency(name = "Russian Ruble", code = "RUB", symbol = "₽"),
        Currency(name = "Indian Rupee", code = "INR", symbol = "₹"),
        Currency(name = "Brazilian Real", code = "BRL", symbol = "R$"),
        Currency(name = "South African Rand", code = "ZAR", symbol = "R"),

    ]
    Currency.objects.bulk_create(currencies)

def add_category_data(apps, schema_editor):
    Category = apps.get_model('webapp', 'Category')
    categories = [

        Category(name = 'Business'),
        Category(name = 'Donations'),
        Category(name = 'Eating Out'),
        Category(name = 'Education'),
        Category(name = 'Entertainment'),
        Category(name = 'Groceries'),
        Category(name = 'Health'),
        Category(name = 'Loan'),
        Category(name = 'Shopping'),
        Category(name = 'Super Contributions'),
        Category(name = 'Taxes'),
        Category(name = 'Transfers & Payments'),
        Category(name = 'Travel'),        
        Category(name = 'Transport'),
        Category(name = 'Other'),
        Category(name = 'Utilities'),

    ]
    Category.objects.bulk_create(categories)

def add_expenses(apps, schema_editor):
    Expense = apps.get_model('webapp', 'Expense')
    Category = apps.get_model('webapp', 'Category')
    Currency = apps.get_model('webapp', 'Currency')

    # Retrieve the Australian Dollar currency from the database
    aud = Currency.objects.get(code="AUD")

    # Retrieve all categories
    categories = list(Category.objects.all())

    # Generate 50 random expenses for April 2024
    expenses = []
    for _ in range(50):
        expense = Expense(
            category=random.choice(categories),
            currency=aud,
            amount=random.uniform(10.0, 2000.0),  # Random expense between $10 and $2000
            date=date(2024, 4, random.randint(1, 30)),  # Random day in April
            description="Autogenerated expense"
        )
        expenses.append(expense)

    Expense.objects.bulk_create(expenses)

def add_income_category_data(apps, schema_editor):
    incomeCategory = apps.get_model('webapp', 'IncomeCategory')
    incomeCategories = [

        incomeCategory(name = 'Salary'),
        incomeCategory(name = 'Wages'),
        incomeCategory(name = 'Commission'),
        incomeCategory(name = 'Interest'),
        incomeCategory(name = 'Sales'),
        incomeCategory(name = 'Investments'),
        incomeCategory(name = 'Gifts'),
        incomeCategory(name = 'Allowances'),
        incomeCategory(name = 'Government Payments'),
                ]
    incomeCategory.objects.bulk_create(incomeCategories)

class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_currency_data, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(add_category_data, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(add_income_category_data, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(add_expenses, reverse_code=migrations.RunPython.noop),
    ]