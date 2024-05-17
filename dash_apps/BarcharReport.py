import dash
import datetime as dt

from dash import dcc, html, Input, Output
from django_plotly_dash import DjangoDash

from services.data import get_category_expense_data
from services.graphs import create_expense_barchart


# Define app
app = DjangoDash('CategoryExpensesBar')

app.layout = html.Div(
    [
        dcc.DatePickerRange(
            id = 'bar-picker-range',
            calendar_orientation = 'horizontal',
            day_size = 39,
            with_portal = False,
            first_day_of_week = 0,
            reopen_calendar_on_clear = True,
            clearable = True,
            number_of_months_shown = 1,
            max_date_allowed = dt.date.today(),



        ),
        dcc.Graph(
            id = 'expense-bar-chart',
            figure = create_expense_barchart(),
        )
    ])

# Callback function
@app.callback(
    Output('expense-bar-chart', 'figure'),
    [
        Input('bar-picker-range', 'start_date'),
        Input('bar-picker-range', 'end_date')
    ]
)

# Function to Update Bar Chart
def update_graph(start_date, end_date):
    print(f"Date Range Changed: {start_date} to {end_date}")
    categories, amounts, percentage = get_category_expense_data(start_date, end_date)
    fig = create_expense_barchart(categories, amounts)
    
    return fig
