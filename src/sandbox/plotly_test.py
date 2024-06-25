from dash import Dash, dcc, html, Input, Output, callback
import sys
import basisklassen_cam as bc
from camcar import CamCar
from flask import Flask, Response
import numpy as np
import matplotlib.pylab as plt
import tensorflow as tf

server = Flask(__name__)
app = Dash(__name__)
cam = bc.Camera()
car = CamCar()



app.layout = html.Div([
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div([
        "Input: ",
        dcc.Input(id='my-input', value='initial value', type='text')
    ]),
    html.Br(),
    html.Div(id='my-output'),

])


@callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):
    return f'Output: {input_value}'


if __name__ == '__main__':
    print(cam.check())
    app.run(debug=True)
