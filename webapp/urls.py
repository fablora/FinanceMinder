from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name = 'index'),
    path('expenses_table/', views.ExpenseHTMxTableView.as_view(), name = 'expenses_htmx')
    #path('add_expense/', views.add_expense, name = 'add_expense'),

]