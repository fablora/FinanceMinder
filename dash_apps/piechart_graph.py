import dash
import datetime as dt

from dash import dcc, html, Output, Input
from django_plotly_dash import DjangoDash

from services.data import get_category_expense_data
from services.graphs import create_expense_piechart

# Define app
app = DjangoDash('categories_expenses_pie')

# Define layout of the app
app.layout = html.Div(
    [
        # Data Picker Ranger component for filtering
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
        # Graph component to display the chart
        dcc.Graph(
            id='expense-pie-chart',
            figure=create_expense_piechart(),
        )
    ])

# Callback function to update the chart based on selected date range
@app.callback(
    Output('expense-pie-chart', 'figure'),
    [
        Input('pie-picker-range', 'start_date'),
        Input('pie-picker-range', 'end_date')
    ]
)

# Function to Update Bar Chart
def update_graph(start_date, end_date):
    '''
    Updates the chart based on selected date range

    Parameters:
    start_date (str): start date of the range
    end_date (str): end date of the range

    Returns:
    plotly.graph_objs._figure.Figure: Updated chart figure
    '''
    try:
        # Log selected range
        print(f"Date Range Changed: {start_date} to {end_date}")

        # Get expenses data for the selected range
        categories, amounts, percentage = get_category_expense_data(start_date, end_date)

        # Create and return updated chart
        fig = create_expense_piechart(categories, amounts, percentage)        
        return fig
    
    except ValueError as e:
        # Catch error
        print(f"Error updating graph: {e}") 

        # Return empty figure
        return create_expense_piechart()

