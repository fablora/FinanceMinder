import dash

from dash import dcc, html
from django_plotly_dash import DjangoDash
from services.graphs import create_expense_piechart

# Define app
app = DjangoDash('CategoryExpensesPie')

app.layout = html.Div(
    [
        dcc.Graph(
            id='expense-pie-chart',
            figure=create_expense_piechart(),
        )
    ])
