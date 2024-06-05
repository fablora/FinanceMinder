import plotly.graph_objects as go
import plotly.express as px
import datetime as dt

from .data import get_category_expense_data, get_monthly_expense_by_category


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

def create_expense_trend_chart():

    df = get_monthly_expense_by_category(start_date = None, end_date = None)
    
    df = df.reset_index()
    

    # Format dates as Year-Month
    df['date'] = df['date'].dt.strftime('%b %Y')

    df = df.melt(id_vars = 'date', var_name = 'category', value_name = 'amount')
    

    # Custom color palette
    custom_colors = [

        '#f49595',  # red
        '#33FF57',  # neon green
        '#a8d9f6',  # blue
        '#FF33FF',  # magenta
        '#33FFF5',  # cyan
        '#F5FF33',  # bright yellow
        '#FFB533',  # orange
        '#B533FF',  # purple
        '#33FF99',  # light green
        '#FF3380',  # pink
        '#33A1FF',  # sky blue
        '#B3FF33',  # light yellow-green
        '#FF8333',  # coral
        '#33FFD6',  # light cyan
        '#e1bbfd'   # violet
        
    ]

    fig = px.line(

        df, 
        x = 'date', 
        y = 'amount', 
        color = 'category',
        labels = {'date': 'Month', 'category': 'Category', 'amount': 'Amount'},
        color_discrete_sequence = custom_colors

        )
    
    fig.update_layout(

    title = 'Monthly Expenses by Category',
    xaxis_title = 'Month',
    yaxis_title = 'Amount in AUD',
    xaxis=dict(tickformat='%b %Y'),  # Format x-axis to show abbreviated month and full year
    paper_bgcolor = 'rgba(0,0,0,0)',
    plot_bgcolor = '#424242',
    font_color = '#e1e4e9'

    )    

    return fig