from data_service import DataService

import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import threading
import time

from sonic_car import SonicCar


data_service = DataService("drive_data.json")
data = data_service.read_data()

df = pd.DataFrame(data)

app = dash.Dash(__name__)


app.layout = html.Div(
    [ 
    html.Button(id="f1_btn", type="button", children="Start Fahrparcour 1", style={"display": "flex", "margin": "1rem auto"}),
    html.Button(id="f2_btn", type="button", children="Start Fahrparcour 2", style={"display": "flex", "margin": "1rem auto"}), 
    html.Button(id="f3_btn", type="button", children="Start Fahrparcour 3", style={"display": "flex", "margin": "1rem auto"}), 
    html.Button(id="f4_btn", type="button", children="Start Fahrparcour 4", style={"display": "flex", "margin": "1rem auto"}),     
    html.H1(children="Last Run", style={"textAlign": "center"}),
    dcc.Graph(id="speed_graph",
        figure={
            'data': [
                {'x': df['time'], 'y': df['speed'], 'type': 'line', 'name': 'Speed'},
            ],
            'layout': {
                'title': 'Speed',
                'xaxis': {
                'tickangle': 45,
                'tickmode': 'auto'},
                'yaxis': {'title': 'Speed'}
            }
        }
    ),
    dcc.Graph(id="obsticle_graph",
        figure={
            'data': [
                {'x': df['time'], 'y': df['obsticle_dist'], 'type': 'line', 'name': 'Obstacle Distance'},
            ],
            'layout': {
                'title': 'Obstacle Distance',
                'xaxis': {
                'tickangle': 45,
                'tickmode': 'auto'},
                'yaxis': {'title': 'Obstacle Distance'}
            }
        }
    ),
    dcc.Graph(id="steering_graph",
        figure={
            'data': [
                {'x': df['time'], 'y': df['wheels_angle'], 'type': 'line', 'name': 'Steering Wheel Angle'},
            ],
            'layout': {
                'title': 'Steering Angle',
                'xaxis': {
                'tickangle': 45,
                'tickmode': 'auto'},
                'yaxis': {'title': 'Steering Angle'}
            }
        }
    ),
     dcc.Graph(
        id='all-graph',
        figure={
            'data': [
                {'x': df['time'], 'y': df['speed'], 'type': 'line', 'name': 'Speed'},
                {'x': df['time'], 'y': df['obsticle_dist'], 'type': 'line', 'name': 'Obstacle Distance in cm'},
                {'x': df['time'], 'y': df['wheels_angle'], 'type': 'line', 'name': 'Steering Angle in ° (forward 90)'},
            ],
            'layout': {
                'title': 'All Values', 
                'xaxis': {
                'tickangle': 45,
                'tickmode': 'auto'},               
                'yaxis': {'title': 'Values'}
            }
        }
    )
])

@app.callback(
    Output("f1_btn", "n_clicks"),
    [Input("f1_btn", "n_clicks")],
    prevent_initial_call=True
)
def run1(n_clicks):
     if n_clicks is not None:
        car = SonicCar()
        try:
            car.fahrparkur_1()
        except Exception as ex:
            print(f"Something's wrong! {ex}")
            car.drive_stop()

@app.callback(
    Output("f2_btn", "n_clicks"),
    [Input("f2_btn", "n_clicks")],
    prevent_initial_call=True
)
def run2(n_clicks):
     if n_clicks is not None:
        car = SonicCar()
        try:
            car.fahrparkur_2()
        except Exception as ex:
            print(f"Something's wrong! {ex}")
            car.drive_stop()
            
@app.callback(
    Output("f3_btn", "n_clicks"),
    [Input("f3_btn", "n_clicks")],
    prevent_initial_call=True,
)
def run3(n_clicks):
     if n_clicks is not None:
        car = SonicCar()
        try:
            car.run_until_obstacle_detected()
        except Exception as ex:
            print(f"Something's wrong! {ex}")
            car.drive_stop()

@app.callback(
    Output(component_id="speed_graph", component_property="figure"),
    Output(component_id="obsticle_graph", component_property="figure"),
    Output(component_id="steering_graph", component_property="figure"),
    Output(component_id="all-graph", component_property="figure"),
    [Input(component_id="f4_btn", component_property="n_clicks")],    
    prevent_initial_call=True,    
)
def run4(n_clicks):
     if n_clicks is not None:
        car = SonicCar()
        try:
            car.run_fahrparcour_4()
            car.steerin_angle = 90
            data_service = DataService("drive_data.json")
            data = data_service.read_data()

            df = pd.DataFrame(data)
            
            speed_figure = {
                'data': [
                    {'x': df['time'], 'y': df['speed'], 'type': 'line', 'name': 'Speed'},
                ],
                'layout': {
                    'title': 'Speed',
                    'xaxis': {
                    'tickangle': 45,
                    'tickmode': 'auto'},
                    'yaxis': {'title': 'Speed'}
                }
            }
            obsticle_figure={
                'data': [
                    {'x': df['time'], 'y': df['obsticle_dist'], 'type': 'line', 'name': 'Obstacle Distance'},
                ],
                'layout': {
                    'title': 'Obstacle Distance',
                    'xaxis': {
                    'tickangle': 45,
                    'tickmode': 'auto'},
                    'yaxis': {'title': 'Obstacle Distance'}
                }
            }
            steering_figure={
                'data': [
                    {'x': df['time'], 'y': df['wheels_angle'], 'type': 'line', 'name': 'Steering Wheel Angle'},
                ],
                'layout': {
                    'title': 'Steering Angle',
                    'xaxis': {
                    'tickangle': 45,
                    'tickmode': 'auto'},
                    'yaxis': {'title': 'Steering Angle'}
                }
            }
            all_graph = {
                'data': [
                    {'y': df['speed'], 'type': 'line', 'name': 'Speed'},
                    {'y': df['obsticle_dist'], 'type': 'line', 'name': 'Obstacle Distance in cm'},
                    {'y': df['wheels_angle'], 'type': 'line', 'name': 'Steering Angle in ° (forward 90)'},
                ],
                'layout': {
                    'title': 'All Values',
                    'yaxis': {'title': 'Values'}
                }
            }
            return speed_figure, obsticle_figure, steering_figure, all_graph
        except Exception as ex:
            print(f"Something's wrong! {ex}")
            car.drive_stop()
            
            
            
if __name__ == '__main__':
    app.run_server(debug=True)