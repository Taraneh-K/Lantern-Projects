import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
from datetime import datetime as dt
import plotly.graph_objs as go
import statsmodels
from flask import Flask


# Step 1. Launch the application

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config['suppress_callback_exceptions'] = True
app.scripts.config.serve_locally = True
server = app.server
# Step 2. Import the dataset


merged_sleep_exercise = pd.read_csv('merged_sleep_exercise.csv')
type_exercise=pd.read_csv('type_exercise.csv')
walk_df=pd.read_csv('walk_df.csv')
by_week_day=pd.read_csv('by_week_day.csv')
#by_date_sum_steps=pd.read_csv('by_date_sum_steps.csv')
#stress_heart=pd.read_csv('stress_heart.csv')

# dropdown options

#opts = [{'label' : i, 'value' : i} for i in features]
features = merged_sleep_exercise.columns[[2,3,4,6,8]]
labels=['Calorie (cal)','Exercise Duration (min)','Time Offset','Sleep Efficiency (%)','Sleep Duration (min)']

#Date chooser
merged_sleep_exercise['start_date'] = pd.to_datetime(merged_sleep_exercise['start_date'], format='%Y-%m-%d')

# Step 3. Create a plotly figure

trace_1 = go.Scatter(x = merged_sleep_exercise.start_date, y = merged_sleep_exercise['calorie'],

                    name = 'Calorie',

                    line = dict(width = 2,

                                color = 'rgb(229, 151, 50)'))

layout = go.Layout(title = '',

                   hovermode = 'closest')

fig = go.Figure(data = [trace_1], layout = layout)
name=""

# Step 4. Create a Dash layout
app.layout = html.Div([
    html.Div([
        html.H1('Analysis of Health Data of a Person'),
        html.P('By: Taraneh Kordi')],style = {'padding' : '50px' ,'backgroundColor' : '#3aaab2'}),

    
    dcc.Tabs(id="tabs-example", value='tab-1-example', children=[
        dcc.Tab(label='Time Series', value='tab-1-example'),
        dcc.Tab(label='Exercise Types', value='tab-2-example'),
        dcc.Tab(label='Walking Calories', value='tab-3-example'),
        dcc.Tab(label='Travel/ No Travel ', value='tab-4-example'),
        dcc.Tab(label='Day of Week', value='tab-5-example'),
        ]),
    html.Div(id='tabs-content-example')
    
    
])



@app.callback(Output('tabs-content-example', 'children'),
              [Input('tabs-example', 'value')]
              
              )


def render_content(tab):
    if tab == 'tab-1-example':
        return tab_1_layout

    elif tab == 'tab-2-example':
        return tab_2_layout

    elif tab == 'tab-3-example':
        return tab_3_layout

    elif tab == 'tab-4-example':
        return tab_4_layout

    elif tab == 'tab-5-example':
        return tab_5_layout

    


tab_1_layout = html.Div([
            html.H3("Tested Parameters over Time"),
            html.P('This graph shows Calorie, Exercise Duration, Time Offset, Sleep Efficiency and Duration over time between the selected time range.'),

            # adding a plot html.H3(id= , children= )

                dcc.Graph(id = 'graph-1-tabs', figure = fig),

                # dropdown

                html.P([

                    html.Label("Choose a feature"),

                    dcc.Dropdown(id = 'opt', options = [{'label':labels[0]  ,'value':features[0]},
                    {'label':labels[1]  ,'value':features[1]},
                    {'label':labels[2]  ,'value':features[2]},
                    {'label':labels[3]  ,'value':features[3]},
                    {'label':labels[4]  ,'value':features[4]}],

                                value = 'calorie'
                                )

                        ], style = {'marginLeft': 10, 'marginRight': 10, 'marginTop': 10, 'marginBottom': 10, 
               'backgroundColor':'#F7FBFE',
               'border': 'thin lightgrey dashed', 'padding': '6px 0px 0px 8px'}),

                # Date Range Picker
                html.P([

                    html.Label("Choose a Time Range"),

                    dcc.DatePickerRange(id='my-date-picker-range',
                    min_date_allowed=dt(2017, 12, 19),
                    max_date_allowed=dt(2019, 5, 10),
                    initial_visible_month=dt(2017, 12, 19),
                    start_date=dt(2017, 12, 19),
                    end_date=dt(2019, 5, 10)),
                    html.Div(id='output-container-date-picker-range')],
                    style = {'marginLeft': 10, 'marginRight': 10, 'marginTop': 10, 'marginBottom': 10, 
               'backgroundColor':'#F7FBFE',
               'border': 'thin lightgrey dashed', 'padding': '6px 0px 0px 8px'})

        ])

tab_2_layout = html.Div([
            html.H3('Calorie vs. Exercise Duration for each Exercise Type'),
            html.P('This graph shows Calories used during each exercise type and its correlation with Exercise Duration. Also, distribution of Calories and Exercise Duration for each exercise type are shown. '),
                dcc.Graph(id='graph-2-tabs',
                figure = px.scatter(type_exercise, x='exercise_duration_minutes', y='calorie',color='type', marginal_y="box",
                marginal_x="box",trendline="ols",labels={'exercise_duration_minutes':"Exercise Duration (min)",'calorie':"Calorie (cal)","type":"Type"})

                    
    
            )
        ])

tab_3_layout = html.Div([
            html.H3('Calorie vs. Walking Duration and Average Spead'),
            html.P('This graph shows correlation between Walking Duration and burnt Calories. Also, we can see the Average Walking Speed for each data point. Moreover, distribution of Calories and Walking Duration are shown. '),
                dcc.Graph(id='graph-3-tabs',
                figure = px.scatter(walk_df, x='exercise_duration_minutes', y='calorie',color='mean_speed', marginal_y="box",
                marginal_x="box",trendline="ols",labels={'exercise_duration_minutes':"Walking Duration (min)",'calorie':"Calorie (cal)",'mean_speed':"Average Speed (m/s)"})
                
            )
        ])

tab_4_layout = html.Div([
            html.H3('Calorie vs. Exercise Duration by Travel Status'),
            html.P('This graph shows correlation between Exercise Duration and burnt Calories for travel times and when the person is not vacation. Also, distribution of Calories and Exercise Duration for 2 situations of being on vacation or not are shown.'),
                dcc.Graph(
                id='graph-4-tabs',
                figure = px.scatter(merged_sleep_exercise, x='exercise_duration_minutes', y='calorie',color='status', marginal_y="violin",
                marginal_x="box",trendline="ols",labels={'exercise_duration_minutes':"Exercise Duration (min)",'calorie':"Calorie (cal)",'status':"Status"})
  
            )
        ])

tab_5_layout = html.Div([
            html.H3('Sleep Efficiency vs. Calorie per day of week'),
            html.P('This graph shows average Sleep Efficiency and amount of Calories burnt for each day of week.'),
                dcc.Graph(
                id='graph-5-tabs',
                figure = px.scatter(by_week_day, x="calorie", y='efficiency', size="sleep_duration", color="day_of_week_y",
                hover_name="day_of_week_y", log_x=True, size_max=60,category_orders={"day_of_week_y": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]},labels={"efficiency":"Sleep Efficiency (%)","calorie":"Calorie (cal)","day_of_week_y":"Day of Week"})
  
            )
        ])



@app.callback(dash.dependencies.Output('graph-1-tabs', 'figure'),

             [dash.dependencies.Input('opt', 'value'),

             dash.dependencies.Input('my-date-picker-range','start_date'),
             dash.dependencies.Input('my-date-picker-range','end_date')
             ])


def update_figure(input1,start_date, end_date):

    df = merged_sleep_exercise
    df['start_date'] = pd.to_datetime(df['start_date'], format='%Y-%m-%d')
    df = df[(df['start_date'] > start_date) & (df['start_date'] < end_date)]
    trace_2 = go.Scatter(x = df['start_date'], y = df[input1], name = 1,
    line = dict(width = 2, color = 'rgb(106, 181, 135)'))
    
    fig = go.Figure(data = trace_2, layout = layout)

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
   

