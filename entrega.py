import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.title("Visualización de datos simulados")

# Control deslizante para definir cuántos puntos generar
cantidad_puntos = st.slider("Elige la cantidad de puntos", min_value=5, max_value=50, value=10)

# Crear valores aleatorios
tiempos = np.sort(np.random.uniform(0, 10, cantidad_puntos))  # Valores de tiempo entre 0 y 10 segundos
voltajes = np.random.uniform(0, 5, cantidad_puntos)  # Valores de voltaje entre 0 y 5V

# Crear un DataFrame con los datos generados
datos = pd.DataFrame({
    "Tiempo (s)": tiempos,
    "Voltaje (V)": voltajes
})

# Mostrar los datos en forma de tabla
st.write("Tabla de datos generados:")
st.dataframe(datos)

# Dibujar la gráfica
figura, eje = plt.subplots()
eje.plot(datos["Tiempo (s)"], datos["Voltaje (V)"], marker="o", linestyle="-")
eje.set_xlabel("Tiempo (s)")
eje.set_ylabel("Voltaje (V)")
eje.set_title("Gráfico de Voltaje en función del Tiempo")
st.pyplot(figura)
    