'''
Libreria para graficar con plotly
'''
import json
import plotly
import plotly.express as px


def area_chart(dataframe, x, y):
    '''
    Función para generar gráficas lineales con area_chart
    '''
    fig = px.area(dataframe, x=x, y=y, title='Suscriptores De Internet Venezuela')
    fig.update_xaxes(rangeslider_visible=True)
    fig.update_yaxes(title=None)
    fig.update_layout(
            hovermode='x',
            paper_bgcolor='#212529',
            plot_bgcolor='#212529',
            font=dict(color='white', size=12),
            width=700,
            height=500,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
                )
            )

    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graph_json
