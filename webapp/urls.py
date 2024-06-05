from django.urls import path, include
from .views import bar_dashboard, pie_dashboard, income_page
from dash_apps import BarcharReport, PiecharReport
from . import views



urlpatterns = [

    path('', views.index, name = 'index'),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    path('expenses_table/', views.ExpenseHTMxTableView.as_view(), name = 'expenses_htmx'),
    path('income-analysis/', income_page, name = 'income_page'),
    path('dashboard/', bar_dashboard, name = 'bar_dashboard' ),
    path('second-dashboard/', pie_dashboard, name = 'pie_dashboard')


]