import dash
from dash import dcc, html
from datetime import datetime
import pandas as pd
from data_service import DataService

data_service = DataService("drive_data.json")

data = data_service.read_data()

df = pd.DataFrame(data)
import os

current_working_directory = os.getcwd()
print("Aktuelles Arbeitsverzeichnis:", current_working_directory)


# Aktueller Dateipfad (Verzeichnis der aktuellen Datei)
current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)
print("Aktueller Dateipfad:", current_file_path)
print("Aktuelles Verzeichnis der Datei:", current_directory)
# "borderRadius": "10px", "marginTop": "2rem"
app = dash.Dash(__name__)
# Layout der Dash-App
app.layout = html.Div(
    [
    html.Img(src='https://cdn.pixabay.com/photo/2017/09/06/20/44/f1-2722971_1280.png', style={"display": "flex", "margin": "0 auto", "width": "400px", "borderRadius": "30px", "marginTop": "2rem"}),
    html.H1(children="Last Run", style={"textAlign": "center"}),
    dcc.Graph(
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
    dcc.Graph(
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
    dcc.Graph(
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
        id='example-graph',
        figure={
            'data': [
                {'y': df['speed'], 'type': 'line', 'name': 'Speed'},
                {'y': df['obsticle_dist'], 'type': 'line', 'name': 'Obstacle Distance'},
                {'y': df['wheels_angle'], 'type': 'line', 'name': 'Steering Angle'},
            ],
            'layout': {
                'title': 'All Values',
                'xaxis': {},
                'yaxis': {'title': 'Values'}
            }
        }
    )
])

# Die App starten
if __name__ == '__main__':
    app.run_server(debug=True)