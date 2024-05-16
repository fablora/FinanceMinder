import dash

from dash import dcc, html
from django_plotly_dash import DjangoDash
from services.graphs import create_expense_barchart

# Define app
app = DjangoDash('CategoryExpensesBar')

app.layout = html.Div(
    [
        dcc.Graph(
            id='expense-bar-chart',
            figure=create_expense_barchart(),
        )
    ])
