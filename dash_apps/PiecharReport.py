import dash
import datetime as dt

from dash import dcc, html, Output, Input
from django_plotly_dash import DjangoDash
from services.data import get_category_expense_data
from services.graphs import create_expense_piechart

# Define app
app = DjangoDash('CategoryExpensesPie')

app.layout = html.Div(
    [
        dcc.DatePickerRange(
            id = 'pie-picker-range',
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
            id='expense-pie-chart',
            figure=create_expense_piechart(),
        )
    ])

# Callback function
@app.callback(
    Output('expense-pie-chart', 'figure'),
    [
        Input('pie-picker-range', 'start_date'),
        Input('pie-picker-range', 'end_date')
    ]
)

# Function to Update Bar Chart
def update_graph(start_date, end_date):
    print(f"Date Range Changed: {start_date} to {end_date}")
    categories, amounts, percentage = get_category_expense_data(start_date, end_date)
    fig = create_expense_piechart(categories, amounts, percentage)
    
    return fig
