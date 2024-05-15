# Generated by Django 5.0 on 2024-05-14 09:46

from django.db import migrations

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


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial')
    ]

    operations = [
        migrations.RunPython(add_currency_data),
        migrations.RunPython(add_category_data)
    ]
