'''
Aplicación flask
'''
from flask import Flask, render_template
import pandas as pd
from charting import area_chart

app = Flask(__name__)

@app.route('/')
def index():
    '''
    Página principal
    '''
    dataframe = pd.read_csv(
            'Suscriptores_internet_Vnzla.csv',
            delimiter=';',
            usecols=[
                'Año',
                'Total Banda Ancha',
                'Total Suscriptores'
                ])
    dataframe = dataframe.groupby(['Año']).sum().reset_index()

    graph_json = area_chart(
            dataframe, 'Año', ['Total Banda Ancha', 'Total Suscriptores']
            )

    return render_template(
            'index.html',
            graph_json=graph_json,
            dataframe=[dataframe.to_html(
                classes='table table-striped table-dark text-end',
                index=False,
                )]
            )

if __name__ == '__main__':
    app.run(debug=True)
