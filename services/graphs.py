import plotly.graph_objects as go
import plotly.express as px
import datetime as dt

from .data import get_category_expense_data

# Data variables
#categories, amounts, percentage = get_category_expense_data()


# Function to create Barchart

def create_expense_barchart(categories = None, amounts = None):
    if categories is None or amounts is None:
        categories, amounts, percentage = get_category_expense_data()

    fig = go.Figure(data = [
        go.Bar(
            x = categories,
            y = amounts,
            hoverlabel = dict(
                bgcolor = 'white'

            ),
            hoverinfo = None,
            hovertemplate = '%{x}: %{y:$.2f}',
            marker_color = '#008ac5',
            marker_line_color = 'rgba(0,0,0,0)',
            name = ""
            )
    ])

    fig.update_layout(
        title = 'Total Expenses by Category',
        paper_bgcolor = 'rgba(0,0,0,0)',
        plot_bgcolor = 'rgb(0,0,0)',
        font_color = '#e1e4e9',
        yaxis = dict(gridcolor = '#283442', zerolinecolor = '#283442')
        #template = 'plotly_dark'
    )

    return fig


# Function to create Piechart

def create_expense_piechart(categories = None, amounts = None, percentage = None):
    if categories is None or amounts is None or percentage is None:
        categories, amounts, percentage = get_category_expense_data()

    fig = px.pie(
        values = percentage,
        names = categories,
        color_discrete_sequence = px.colors.sequential.RdBu
        #color = categories,
        )
    
    fig.update_traces(
        customdata = amounts,
        hoverlabel = dict(
            bgcolor = 'white'

        ),
        hovertemplate = '<b>%{label}</b><br>Amount: $%{customdata[0]}'
    )
    
    fig.update_layout(
        title = 'Expenses Percentage Distribution',
        template = 'plotly_white',
        height = 750,
        width = 1000,
    )

    return fig