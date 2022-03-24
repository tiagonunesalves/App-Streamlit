from matplotlib.pyplot import title, xlabel, ylabel
import streamlit as st
import pandas as pd
import plotly.express as px

#Leitura do dataframe
df = pd.read_csv('Carros.csv', delimiter=';')

#Configuração da página
st.set_page_config(
    page_title='Dashboard Veículos',
    page_icon=':bar_chart:',
    layout='centered'
    )

st.title(':bar_chart: Dashboard dos Veículos')

st.sidebar.subheader('FILTROS')

filtro_zero = st.sidebar.multiselect(
    label='Veículo Zero km?',
    options=df['Zero_km'].unique(),
    default=df['Zero_km'].unique()
)

filtro_motor = st.sidebar.multiselect(
    label ='Selecione o tipo de motor:',
    options=df['Motor'].unique(),
    default=df['Motor'].unique())

df_filtrado = df.query(f'Motor == @filtro_motor and Zero_km == @filtro_zero')

esquerda, centro, direita = st.columns(3)

media_valor = round(df_filtrado['Valor'].mean(), 2)
try:
    media_km = int(round(df_filtrado['Quilometragem'].mean(), 0))
    ano_medio = int(round(df_filtrado['Ano'].mean(), 0))
    idade_media = 2019 - ano_medio

except:
    media_km = 0
    ano_medio = 0
    idade_media = 0

with esquerda:
    st.subheader(':dollar: Valor Médio')
    st.subheader(f':moneybag: {media_valor}')

with centro:
    st.subheader(':calendar: Ano Médio')
    st.subheader(f':arrow_right: {ano_medio}')

with direita:
    st.subheader(':oncoming_automobile: km Médio')
    st.subheader(f':arrow_right: {media_km}') 



grafico_barras = px.bar(
                    df_filtrado[['Nome', 'Valor']],
                    x='Valor',
                    y='Nome',
                    orientation='h',
                    text='Valor',
                    width=700,
                    height=600
                    )

st.plotly_chart(grafico_barras)


#st.bar_chart(df_filtrado['Valor'])

#st.dataframe(df_filtrado)