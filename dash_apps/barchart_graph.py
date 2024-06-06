import dash
import datetime as dt

from dash import dcc, html, Input, Output
from django_plotly_dash import DjangoDash

from services.data import get_category_expense_data
from services.graphs import create_expense_barchart


# Define the app
app = DjangoDash('categories_expenses_bar')

# Define layout of the app
app.layout = html.Div(
    [
        # Data Picker Ranger component for filtering
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
        # Graph component to display the chart
        dcc.Graph(
            id = 'expense-bar-chart',
            figure = create_expense_barchart(),
            style={ 'border-radius':'15px', 'background-color':'black'}
        )
    ])

# Callback function to update the chart based on selected date range
@app.callback(
    Output('expense-bar-chart', 'figure'),
    [
        Input('bar-picker-range', 'start_date'),
        Input('bar-picker-range', 'end_date')
    ]
)
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
        fig = create_expense_barchart(categories, amounts)        
        return fig
    
    except ValueError as e:
        # Catch error
        print(f"Error updating graph: {e}") 

        # Return empty figure
        return create_expense_barchart()

