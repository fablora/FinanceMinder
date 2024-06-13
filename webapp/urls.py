from django.urls import path, include
from .views import bar_dashboard, pie_dashboard, income_page, line_dashboard
from dash_apps import barchart_graph, piechart_graph, line_graph#, adjusted_salary_graph
from . import views



urlpatterns = [

    path('', views.index, name = 'index'),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    path('expenses_table/', views.ExpenseHTMxTableView.as_view(), name = 'expenses_htmx'),
    path('income-analysis/', income_page, name = 'income_page'),
    path('dashboard/', bar_dashboard, name = 'bar_dashboard' ),
    path('second-dashboard/', pie_dashboard, name = 'pie_dashboard'),
    path('line-dashboard/', line_dashboard, name = 'line_dashboard')

]