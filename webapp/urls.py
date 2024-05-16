from django.urls import path, include
from .views import bardashboard, piedashboard
from dash_apps import BarcharReport, PiecharReport
from . import views



urlpatterns = [

    path('', views.index, name = 'index'),
    path('django_plotly_dash/', include('django_plotly_dash.urls')),
    path('expenses_table/', views.ExpenseHTMxTableView.as_view(), name = 'expenses_htmx'),
    path('dashboard/', bardashboard, name = 'bardashboard' ),
    path('second-dashboard/', piedashboard, name = 'piedashboard' )
    #path('add_expense/', views.add_expense, name = 'add_expense'),

]