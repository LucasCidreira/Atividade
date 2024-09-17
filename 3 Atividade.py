import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from dash import Dash, html, dcc

df = pd.read_csv('C:/Users/lucas/Projeto EBAC/Planilhas/ecommerce_estatistica.csv')


## Histograma
fig1= px.histogram(df, x='Nota', y='Desconto', color='Gênero' )
fig1.update_layout(
    title='Nota vs Desconto por Gênero',
    xaxis_title='Nota',
    yaxis_title='Desconto'
        )


# Dispersão
fig2 = px.scatter(df, x='Material_Cod', y='Preço', color='Preço')
fig2.update_layout(
    title='Dispersao de Material e Preço',
    xaxis_title='Material',
    yaxis_title='Preço'
    )


# Grafico de Barras
fig3 = px.bar(df, x="Nota", y="N_Avaliações", color="Preço", barmode="group")
fig3.update_layout(
    title='Qtd de Nota',
    xaxis_title='Nota',
    yaxis_title='Quantidade',
    legend_title='Preço',
    plot_bgcolor='rgba(222, 255, 253, 1)',  # Fundo Interno
    paper_bgcolor='rgba(186, 245, 241, 1)'  # Fundo externo
    )
#grafico de pizza

fig4 = px.pie(df, values='Nota', names='Nota', title='Quantidade Notas')

# Grafico de densidade

fig5 = px.histogram(df, x='Preço', color ='Material_Cod', marginal="rug", hover_data=df.columns)


#criar app

app = Dash(__name__)

app.layout = html.Div([
    dcc.Graph(figure=fig1),
    dcc.Graph(figure=fig2),
    dcc.Graph(figure=fig3),
    dcc.Graph(figure=fig4),
    dcc.Graph(figure=fig5)])

# executa app
app.run_server(debug=True, port=8050) #default 8050