import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
from glob import glob

# Use this file to read in your data and prepare the plotly visualizations. The path to the data files are in
# `data/file_name.csv`


def clean_data():
    """ Reads the dataframes and returns a clean df """
    
#    filenames = glob('data/*.csv')
#    dataframes = [pd.read_csv(f) for f in filenames]

    # need to unified the columns names
#    for i in range(0,len(dataframes)):
#        dataframes[i].columns = [label.replace(' ','_') for label in dataframes[i].columns]
#        dataframes[i].columns = [label.replace('/','_') for label in dataframes[i].columns]
#        dataframes[i] = dataframes[i][['Province_State', 'Country_Region', 'Last_Update', "Confirmed", 'Deaths', 'Recovered']]

#    df = pd.concat(dataframes, ignore_index=True)
#    df['Last_Update'] = pd.to_datetime(df['Last_Update'])
#    df['Date'] = df['Last_Update'].dt.date
#    df.drop('Last_Update',axis=1, inplace =True)

    df = pd.read_csv('data/ocup_madrid_2020.csv')
    df19 = pd.read_csv('data/ocup_madrid_2019.csv')
    return df, df19

def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # first chart plots arable land from 1990 to 2015 in top 10 economies 
    # as a line chart

    df, df19 = clean_data()

#    Arg = df[df.Country_Region == 'Argentina'].groupby('Date', as_index = False)[['Confirmed','Deaths', 'Recovered']].max()
    
    graph_one = []    
#    graph_one.append(
#        go.Figure(data=[
#    go.Bar(name='Feb', x=df['Period'].tolist(), y=df['available_feb'].tolist()),
#    go.Bar(name='March', x=df['Period'].tolist(), y=df['available_mar'].tolist())
#        ])
#    )

    graph_one.append(go.Bar(name='February 2020', x=df['Period'].tolist(), y=df['available_feb'].tolist()))
    graph_one.append(go.Bar(name='March 2020', x=df['Period'].tolist(), y=df['available_mar'].tolist()))



    layout_one = dict(title = 'Bookings for each period according to February and March data - 2020',
                xaxis = dict(title = 'Period', tickangle = 45, type = 'category', showticklabels = True),
                yaxis = dict(title = 'Booking rate'),
                )

# second chart plots ararble land for 2015 as a bar chart    
    graph_two = []

    graph_two.append(go.Bar(name='February 2019', x=df19['Period'].tolist(), y=df19['available_feb'].tolist()))
    graph_two.append(go.Bar(name='March 2019', x=df19['Period'].tolist(), y=df19['available_mar'].tolist()))



    layout_two = dict(title = 'Bookings for each period according to February and March data - 2019',
                xaxis = dict(title = 'Period', tickangle = 45, type = 'category', showticklabels = True),
                yaxis = dict(title = 'Booking rate'),
                )


# third chart plots percent of population that is rural from 1990 to 2015
    graph_three = []
    graph_three.append(
      go.Bar(
      x = ['a', 'b', 'c', 'd', 'e'],
      y = [12, 9, 7, 5, 1],
      )
    )

    layout_three = dict(title = 'Recovered',
                xaxis = dict(title = 'Date'),
                yaxis = dict(title = 'Recovered')
                       )
    
# fourth chart shows rural population vs arable land
    graph_four = []
    
    graph_four.append(
      go.Bar(
      x = ['a', 'b', 'c', 'd', 'e'],
      y = [12, 9, 7, 5, 1],
      )
    )

    layout_four = dict(title = 'Deaths',
                xaxis = dict(title = 'Date'),
                yaxis = dict(title = 'Deaths'),
                )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures
