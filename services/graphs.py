import plotly.graph_objects as go
import plotly.express as px

from .data import get_category_expense_data

# Data variables
categories, amounts, percentage = get_category_expense_data()


# Function to create Barchart

def create_expense_barchart():

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
            name = ""
            )
    ])

    fig.update_layout(
        title = 'Total Expenses by Category',
        template = 'plotly_dark'
    )

    return fig

# Function to create Piechart

def create_expense_piechart():
    fig = px.pie(
        values = percentage,
        names = categories,
        color = categories,
        )
    
    fig.update_traces(
        customdata = amounts,
        hovertemplate = '<b>%{label}</b><br>Amount: $%{customdata[0]}'
    )
    
    fig.update_layout(
        title = 'Expenses Percentage Distribution',
        template = 'plotly_white',
        height = 750,
        width = 1000,
    )
    print("Categories:", categories)
    print("Amounts:", amounts)
    print("Percentage:", percentage)

    return fig