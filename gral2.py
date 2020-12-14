import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import dash_bootstrap_components as dbc

from app import app
from apps import general_functions as gf
#from apps_igf import func_gral

main_layout = dbc.Container([
    dbc.Row([
        #Controles
        dbc.Col([
            html.P("Selecciona un RFC:"),
            dcc.Dropdown(
                id="gral_drp_0",
                options=[{"label": "RFC001", "value":"RFC001"},
                        {"label": "RFC002", "value":"RFC002"},
                        {"label": "RFC003", "value":"RFC003"}]
            ),
            html.Br(),
            html.P("Año:", className="control_label"),
            dcc.Dropdown(
                id="gral_drp_1",
                options=[{"label": "2020", "value":"2020"},
                        {"label": "2019", "value":"2019"},
                        {"label": "2018", "value":"2018"}],
            ),
            html.Br(),
            html.P("Rango de meses:", className="control_label"),
            dcc.RangeSlider(
                id="gral_drp_2",
                min=1,
                max=12,
                value=[1, 12],
            ),
            html.Br(),
            html.P("Tipo de Documento:", className="control_label"),
            dcc.Dropdown(
                id="gral_drp_3",
                options=[{"label": "Pago", "value":"Pago"},
                        {"label": "Egreso", "value":"Egreso"},
                        {"label": "Ingreso", "value":"Ingreso"}],
            ),
            html.Br(),
            html.P("Tipo de Moneda:", className="control_label"),
            dcc.RadioItems(
                id="gral_drp_4",
                options=[
                    {"label": "Pesos MXN  ", "value": "MXN"},
                    {"label": "Dolares USD  ", "value": "USD"},],
                    labelStyle={"display": "inline-block"},
            ),
        ],className='col-md-3', style={'border-radius': '5px','background-color': '#f9f9f9'}),
        #Montos
        dbc.Col([
            html.H1("MONTOS", className='text-center'),
            gf.mosaico("#00cc96", "Monto Total Emision", "gral_msc_mon_1"),
            gf.mosaico("#00cc96", "Monto Total Recepcion", "gral_msc_mon_2"),
            html.Div(
            [dcc.Graph(id="gral_grf_mts_1",
                        config=dict(displayModeBar=False))],
            ),
        ],className='col-md-8', width={'offset':1})
    ]),
    html.Br(),
    dbc.Row([
        #Facturas
        dbc.Col([
            html.H1("FACTURAS", className='text-center'),
            gf.mosaico("#00cc96", "Cantidad de Facturas Emitidas", "gral_msc_fac_1"),
            gf.mosaico("#00cc96", "Cantidad de Facturas Recibidas", "gral_msc_fac_2"),
            html.Div(
            [dcc.Graph(id="gral_grf_fac_1",
                        config=dict(displayModeBar=False))],
            ),
        ],className='col-md-8', width={'offset':4})
    ])
],fluid=True)

layout = html.Div([
    html.Div([main_layout]),
])

