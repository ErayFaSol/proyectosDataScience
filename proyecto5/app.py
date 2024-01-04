import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('proyecto5/vehicles_us.csv') # leer los datos
encabezado = st.header('Proyecto sprint 5: Herramientas de desarrollo de software')
hist_button = st.checkbox('Construir histograma') # crear un botón
disp_button = st.checkbox('Construir diagrama de dispersion')


if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if disp_button:
    st.write('Creación de un diagrama de dispersion para el conjunto de datos de anuncios de venta de coches')

    fig = px.scatter(car_data, x="odometer", y="price")

    st.plotly_chart(fig, use_container_width=True )