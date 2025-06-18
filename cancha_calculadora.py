import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

st.set_page_config(page_title="Cancha Deportiva - Calculadora V1", layout="centered")
st.title("🏟️ Cancha Deportiva - Calculadora V1")

# Datos de entrada
tipo_cancha = st.selectbox("Tipo de cancha:", ["Fútbol 11 (reglamentaria)"])
ancho = st.number_input("Ancho (en metros)", min_value=1.0, step=0.5, value=68.0)
largo = st.number_input("Largo (en metros)", min_value=1.0, step=0.5, value=105.0)

modelo_pasto = st.selectbox(
    "Modelo de pasto sintético:",
    ["Basic 15mm - $5.040/m²", "Vivo 30mm - $8.900/m²", "Royal 40mm - $8.415/m²", "Prime 40mm - $10.900/m²"]
)
precio_pasto = {
    "Basic 15mm - $5.040/m²": 5040,
    "Vivo 30mm - $8.900/m²": 8900,
    "Royal 40mm - $8.415/m²": 8415,
    "Prime 40mm - $10.900/m²": 10900
}[modelo_pasto]

rollo_ancho = st.radio("Ancho del rollo:", [2, 4])

# Accesorios
arcos = st.checkbox("Arcos (x2)", value=False)
malla = st.checkbox("Malla perimetral", value=False)
pintura = st.checkbox("Pintura de demarcación", value=False)

if ancho and largo:
    m2 = ancho * largo
    rollos = int(np.ceil(ancho / rollo_ancho) * np.ceil(largo / 25))
    total_pasto = m2 * precio_pasto

    total_accesorios = 0
    if arcos: total_accesorios += 120000
    if malla: total_accesorios += m2 * 500
    if pintura: total_accesorios += 25000
    total_final = total_pasto + total_accesorios

    # Visualización de cancha reglamentaria
    fig, ax = plt.subplots(figsize=(largo * 0.1, ancho * 0.1))
    ax.set_xlim(0, largo)
    ax.set_ylim(0, ancho)
    ax.set_aspect('equal')
    ax.add_patch(patches.Rectangle((0, 0), largo, ancho, facecolor='green'))

    # Líneas reglamentarias
    ax.plot([0, largo], [0, 0], color='white', lw=2)
    ax.plot([0, largo], [ancho, ancho], color='white', lw=2)
    ax.plot([0, 0], [0, ancho], color='white', lw=2)
    ax.plot([largo, largo], [0, ancho], color='white', lw=2)

    ax.plot([largo / 2, largo / 2], [0, ancho], color='white', lw=2)
    ax.add_patch(patches.Circle((largo / 2, ancho / 2), 9.15, fill=False, edgecolor='white', lw=2))
    ax.plot([largo / 2], [ancho / 2], 'wo')

    for x in [0, largo - 16.5]:
        ax.add_patch(patches.Rectangle((x, (ancho - 40.32) / 2), 16.5, 40.32, fill=False, edgecolor='white', lw=2))
    for x in [0, largo - 5.5]:
        ax.add_patch(patches.Rectangle((x, (ancho - 18.32) / 2), 5.5, 18.32, fill=False, edgecolor='white', lw=2))

    ax.plot([11], [ancho / 2], 'wo')
    ax.plot([largo - 11], [ancho / 2], 'wo')
    ax.add_patch(patches.Arc((11, ancho / 2), 18.3, 18.3, theta1=308, theta2=52, color='white', lw=2))
    ax.add_patch(patches.Arc((largo - 11, ancho / 2), 18.3, 18.3, theta1=128, theta2=232, color='white', lw=2))

    for cx, cy in [(0, 0), (0, ancho), (largo, 0), (largo, ancho)]:
        ax.add_patch(patches.Arc((cx, cy), 2, 2, theta1=0, theta2=90, color='white', lw=1))

    ax.set_title("Vista previa de cancha reglamentaria")
    ax.axis('off')
    st.pyplot(fig)

    # Resumen
    st.markdown("## 🧾 Resumen")
    st.markdown(f"- Modelo de pasto: **{modelo_pasto}**")
    st.markdown(f"- Área: **{m2:.2f} m²**")
    st.markdown(f"- Rollos de {rollo_ancho}m: **{rollos}**")
    st.markdown(f"- Costo pasto: **${total_pasto:,.0f}**")
    st.markdown(f"- Costo accesorios: **${total_accesorios:,.0f}**")
    st.markdown(f"### ✅ Total estimado: **${total_final:,.0f}**")
