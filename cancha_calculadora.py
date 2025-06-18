import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

st.set_page_config(page_title="Cancha Deportiva - Calculadora V1", layout="centered")
st.title("🏟️ Cancha Deportiva - Calculadora V1")

# Selección de tipo de cancha
tipo_cancha = st.selectbox(
    "Selecciona el tipo de cancha:",
    ["Fútbol 5", "Fútbol 7", "Fútbol 11", "Multicancha", "Otro"]
)

# Dimensiones
st.markdown("### Dimensiones de la cancha")
ancho = st.number_input("Ancho (en metros)", min_value=1.0, step=0.5)
largo = st.number_input("Largo (en metros)", min_value=1.0, step=0.5)

# Mostrar visual solo si hay dimensiones
if ancho > 0 and largo > 0:

    # Cálculos visuales
    fig_width = largo * 0.15
    fig_height = ancho * 0.15
    fig, ax = plt.subplots(figsize=(fig_width, fig_height))
    ax.set_xlim(0, largo)
    ax.set_ylim(0, ancho)
    ax.set_aspect('equal')

    # Pasto
    ax.add_patch(patches.Rectangle((0, 0), largo, ancho, facecolor='green'))

    # Línea perimetral
    ax.plot([0, largo], [0, 0], color='white', linewidth=2)
    ax.plot([0, largo], [ancho, ancho], color='white', linewidth=2)
    ax.plot([0, 0], [0, ancho], color='white', linewidth=2)
    ax.plot([largo, largo], [0, ancho], color='white', linewidth=2)

    # Línea media
    ax.plot([largo / 2, largo / 2], [0, ancho], color='white', linestyle='-', linewidth=2)

    # Círculo central
    circulo = patches.Circle((largo / 2, ancho / 2), radius=3, fill=False, color='white', linewidth=2)
    ax.add_patch(circulo)

    # Áreas chicas (5 metros desde línea y 3 de ancho)
    area_largo = 5
    area_ancho = 3
    ax.add_patch(patches.Rectangle((0, (ancho - area_ancho) / 2), area_largo, area_ancho, fill=False, edgecolor='white', linewidth=2))
    ax.add_patch(patches.Rectangle((largo - area_largo, (ancho - area_ancho) / 2), area_largo, area_ancho, fill=False, edgecolor='white', linewidth=2))

    # Punto penal
    ax.plot([6], [ancho / 2], 'wo')  # lado izquierdo
    ax.plot([largo - 6], [ancho / 2], 'wo')  # lado derecho

    ax.set_title("Vista previa de la cancha")
    ax.axis('off')
    st.pyplot(fig)
