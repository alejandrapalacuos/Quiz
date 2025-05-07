import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Aquí va tu lógica para el quiz...

# Ejemplo de visualización con matplotlib:
def plot_results(data):
    fig, ax = plt.subplots()
    ax.pie(data, labels=["Nostálgico", "Maximalista", "Minimalista"], autopct='%1.1f%%')
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)

# Simulación de resultados
data = [50, 30, 20]  # Estos valores son solo un ejemplo

# Mostrar la gráfica
plot_results(data)
