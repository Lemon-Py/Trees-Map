from flask import Flask, render_template
import pandas as pd

data = pd.read_csv('arbolado-publico-lineal.csv', delimiter=';')
print(data.shape)

polen_trees = ['PLATANUS']

polen_data = data.loc[data['NOMBRE_GEN'].isin(polen_trees)]
no_polen_data = data.loc[~data['NOMBRE_GEN'].isin(polen_trees)]

print (polen_data.shape)
print (no_polen_data.shape)

polen_data['LAT'] = pd.to_numeric(polen_data['LAT'].str.replace(',', '.'))
polen_data['LONG'] = pd.to_numeric(polen_data['LONG'].str.replace(',', '.'))
polen_data_coords = polen_data[['LAT', 'LONG']]

print(polen_data_coords.shape)
# polen_data_coords = polen_data_coords[1:2000]

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html', polen_data_coords=polen_data_coords)

app.run(debug=True)
