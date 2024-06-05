import dash
import datetime as dt

from dash import dcc, html, Input, Output
from django_plotly_dash import DjangoDash

from services.graphs import create_expense_trend_chart


# Define app
app = DjangoDash('monthly_expenses_chart')

app.layout = html.Div(
    [
        dcc.Graph(
            id = 'monthly-line-chart',
            figure = create_expense_trend_chart(),
            style={ 'border-radius':'15px', 'background-color':'black'}
        )
    ]
)
