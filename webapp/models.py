from django.db import models

# Currency model
class Currency(models.Model):
    name = models.CharField(max_length = 50)
    code = models.CharField(max_length = 3)
    symbol = models.CharField(max_length = 5)

    def __str__(self):
        return f"{self.name} ({self.code})"

# Expense Category model
class Category(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

# Expense model
class Expense(models.Model):
    category =      models.ForeignKey(Category, on_delete = models.CASCADE)
    currency =      models.ForeignKey(Currency, on_delete = models.CASCADE)
    amount =        models.DecimalField(max_digits = 10, decimal_places = 2)
    date =          models.DateField()
    description =   models.TextField(blank  = True, null = True)

    def __str__(self):
        return f"{self.date} - {self.amount} {self.currency} / {self.category}"