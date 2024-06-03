from django.urls import path, include
from .views import barDashboard, pieDashboard
from dash_apps import BarcharReport, PiecharReport
from . import views



urlpatterns = [

    path('', views.index, name = 'index'),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    path('expenses_table/', views.ExpenseHTMxTableView.as_view(), name = 'expenses_htmx'),
    path('dashboard/', barDashboard, name = 'bar_dashboard' ),
    path('second-dashboard/', pieDashboard, name = 'pie_dashboard' )


]