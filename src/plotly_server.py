import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from car_sensor import SensorCar
from utilities.data_service import DataService
from parcours.parcour_1 import ParcourOne as p1
from parcours.parcour_2 import ParcourTwo as p2
from parcours.parcour_3 import ParcourThree as p3
from parcours.parcour_4 import ParcourFour as p4
from parcours.parcour_5 import ParcourFive as p5
from parcours.parcour_6 import ParcourSix as p6

car = SensorCar()

data_service = DataService("log/drive_data.json")
data = data_service.read_data()

df = pd.DataFrame(data)

app = dash.Dash(__name__)


app.layout = html.Div(    
    [
    html.Button(id="f1_btn", type="button", children="Fahrparcour 1", style={"position": "fixed", "top": "1rem", "left": "1rem", "padding": "1rem", "backgroundColor": "#333", "color": "#FFF", "zIndex": "100" }),
    
    html.Button(id="f2_btn", type="button", children="Fahrparcour 2", style={"position": "fixed", "top": "1rem", "left": "11rem", "padding": "1rem", "backgroundColor": "#333", "color": "#FFF", "zIndex": "100" }), 
    
    html.Button(id="f3_btn", type="button", children="Fahrparcour 3", style={"position": "fixed", "top": "1rem", "left": "21rem", "padding": "1rem", "backgroundColor": "#333", "color": "#FFF", "zIndex": "100" }), 
    
    html.Button(id="f4_btn", type="button", children="Fahrparcour 4", style={"position": "fixed", "top": "1rem", "left": "31rem", "padding": "1rem", "backgroundColor": "#333", "color": "#FFF", "zIndex": "100" }),
    
    html.Button(id="f5_btn", type="button", children="Fahrparcour 5", style={"position": "fixed", "top": "1rem", "left": "41rem", "padding": "1rem", "backgroundColor": "#333", "color": "#FFF", "zIndex": "100" }),  
    
    html.Button(id="f6_btn", type="button", children="Fahrparcour 6", style={"position": "fixed", "top": "1rem", "left": "51rem", "padding": "1rem", "backgroundColor": "#333", "color": "#FFF", "zIndex": "100" }),  
    
    html.Button(id="stop_btn", type="button", children="Emergency Stop", style={"position": "fixed", "top": "5rem", "left": "1rem", "padding": "4rem 1.5rem", "backgroundColor": "#FF6868", "color": "#FFF", "zIndex": "100", "border": "0px", "borderRadius":"50%"}),     
    html.H1(children="Last Run Log Data", style={"textAlign": "center","marginTop": "10rem"}),
    
     dcc.Graph(
        id='all-graph',
        figure={
            'data': [
                {'x': df['time'], 'y': df['speed'], 'type': 'line', 'name': 'Speed'},
                {'x': df['time'], 'y': df['obsticle_dist'], 'type': 'line', 'name': 'Obstacle Distance in cm'},
                {'x': df['time'], 'y': df['wheels_angle'], 'type': 'line', 'name': 'Steering Angle in ° (forward 90)'},
            ],
            'layout': {
                'title': 'Ultrasonic Values', 
                'xaxis': {
                'tickangle': 45,
                'tickmode': 'auto'},               
                'yaxis': {'title': 'Values'}
            }
        }
    )
     ,
     dcc.Graph(
        id='sensors',
        figure={
            'data': [
                {'x': df['time'], 'y': df['sensor_values'].apply(lambda x: x["sensor1"]), 'type': 'line', 'name': 'Far Left Sensor'},
                {'x': df['time'], 'y': df['sensor_values'].apply(lambda x: x["sensor2"]), 'type': 'line', 'name': 'Middle Left Sensor'},
                {'x': df['time'], 'y': df['sensor_values'].apply(lambda x: x["sensor3"]), 'type': 'line', 'name': 'Middle Sensor'},
                {'x': df['time'], 'y': df['sensor_values'].apply(lambda x: x["sensor4"]), 'type': 'line', 'name': 'Middle Right Sensor'},
                {'x': df['time'], 'y': df['sensor_values'].apply(lambda x: x["sensor5"]), 'type': 'line', 'name': 'Far Right Sensor'}
            ],
            'layout': {
                'title': 'IR Sensors',
                'xaxis': {
                    'tickangle': 45,
                    'tickmode': 'linear'
                },
                'yaxis': {'title': 'Brightness'}
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
        try:
            p1(car).run()

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
        try:
             p2(car).run()
             
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
        try:
            p3(car).run()
            car.steerin_angle = 90            
            
        except Exception as ex:
            print(f"Something's wrong! {ex}")
            car.drive_stop()

@app.callback(    
    Output(component_id="all-graph", component_property="figure", allow_duplicate=True),
    [Input(component_id="f4_btn", component_property="n_clicks")],    
    prevent_initial_call=True,    
)
def run4(n_clicks):
     if n_clicks is not None:
        try:            
            p4(car).run()
            car.steerin_angle = 90
            data = data_service.read_data()
            
            df = pd.DataFrame(data)            
           
            all_graph = {
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
            return all_graph
        except Exception as ex:
            print(f"Something's wrong! {ex}")
            car.drive_stop()
 
@app.callback(
    Output(component_id="all-graph", component_property="figure", allow_duplicate=True),
    Output(component_id="sensors", component_property="figure"),
    [Input(component_id="f5_btn", component_property="n_clicks")],
    prevent_initial_call=True
)
def run5(n_clicks):
     if n_clicks is not None:
        try:
            p5(car).run()
            data = data_service.read_data()
            df = pd.DataFrame(data)
            
            all_graph = {
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
            sensors= {
                'data': [
                    {'x': df['time'], 'y': df['sensor_values'].apply(lambda x: x["sensor1"]), 'type': 'line', 'name': 'Far Left Sensor'},
                    {'x': df['time'], 'y': df['sensor_values'].apply(lambda x: x["sensor2"]), 'type': 'line', 'name': 'Middle Left Sensor'},
                    {'x': df['time'], 'y': df['sensor_values'].apply(lambda x: x["sensor3"]), 'type': 'line', 'name': 'Middle Sensor'},
                    {'x': df['time'], 'y': df['sensor_values'].apply(lambda x: x["sensor4"]), 'type': 'line', 'name': 'Middle Right Sensor'},
                    {'x': df['time'], 'y': df['sensor_values'].apply(lambda x: x["sensor5"]), 'type': 'line', 'name': 'Far Right Sensor'}
                ],
                'layout': {
                    'title': 'IR Sensors',
                    'xaxis': {
                        'tickangle': 45,
                        'tickmode': 'linear'
                    },
                    'yaxis': {'title': 'Brightness'}
                    }
                }
            
            return all_graph, sensors 
        
        except Exception as ex:
            print(f"Something's wrong! {ex}")
            car.drive_stop() 
            
@app.callback(
    Output(component_id="all-graph", component_property="figure", allow_duplicate=True),
    Output(component_id="sensors", component_property="figure", allow_duplicate=True),
    [Input(component_id="f6_btn", component_property="n_clicks")],
    prevent_initial_call=True
)
def run6(n_clicks):
     if n_clicks is not None:
        try:
            p6(car).run()
            data = data_service.read_data()
            df = pd.DataFrame(data)
            
            all_graph = {
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
            sensors={
                'data': [
                    {'x': df['time'], 'y': df['sensor_values'].apply(lambda x: x["sensor1"]), 'type': 'line', 'name': 'Far Left Sensor'},
                    {'x': df['time'], 'y': df['sensor_values'].apply(lambda x: x["sensor2"]), 'type': 'line', 'name': 'Middle Left Sensor'},
                    {'x': df['time'], 'y': df['sensor_values'].apply(lambda x: x["sensor3"]), 'type': 'line', 'name': 'Middle Sensor'},
                    {'x': df['time'], 'y': df['sensor_values'].apply(lambda x: x["sensor4"]), 'type': 'line', 'name': 'Middle Right Sensor'},
                    {'x': df['time'], 'y': df['sensor_values'].apply(lambda x: x["sensor5"]), 'type': 'line', 'name': 'Far Right Sensor'}
                ],
                'layout': {
                    'title': 'IR Sensors',
                    'xaxis': {
                        'tickangle': 45,
                        'tickmode': 'linear'
                    },
                    'yaxis': {'title': 'Brightness'}
                    }
                }
            
            return all_graph, sensors
        except Exception as ex:
            print(f"Something's wrong! {ex}")
            car.drive_stop()        
            
@app.callback(
    Output("stop_btn", "n_clicks"),
    [Input("stop_btn", "n_clicks")],
    prevent_initial_call=True
)
def stop(n_clicks):
     if n_clicks is not None:
        try:
            car.emergency_stop = True            
                       
        except Exception as ex:
            print(f"Something's wrong! {ex}")
            car.drive_stop() 
            
if __name__ == '__main__':
    app.run_server(debug=True)