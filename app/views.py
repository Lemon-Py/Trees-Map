from app import app
from flask import render_template

import pandas as pd

data = pd.read_csv('arbolado-publico-lineal.csv', delimiter=';')

data['LAT'] = pd.to_numeric(data['LAT'].str.replace(',', '.'))
data['LONG'] = pd.to_numeric(data['LONG'].str.replace(',', '.'))

polen_trees = ['PLATANUS']

polen_data = data.loc[data['NOMBRE_GEN'].isin(polen_trees)]
no_polen_data = data.loc[~data['NOMBRE_GEN'].isin(polen_trees)]

polen_data_coords = polen_data[['LAT', 'LONG']]

citrus_lemon = no_polen_data[no_polen_data['NOMBRE_CIE'] == "CITRUS LIMON"][['LAT', 'LONG']]
mora_data = no_polen_data[no_polen_data['NOMBRE_CIE'] == 'MORUS ALBA'][['LAT', 'LONG']]
orange_data = no_polen_data[no_polen_data['NOMBRE_CIE'] == 'CITRUS SINENSIS'][['LAT', 'LONG']]

coord_data = [polen_data_coords, citrus_lemon, mora_data, orange_data]
@app.route('/')
def index():
    return render_template('index.html', data=coord_data)

