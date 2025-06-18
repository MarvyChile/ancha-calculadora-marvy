import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

st.set_page_config(page_title="Cancha Deportiva - Calculadora V1", layout="centered")
st.title("🏟️ Cancha Deportiva - Calculadora V1")

# Entrada de datos
tipo_cancha = st.selectbox("Tipo de cancha:", ["Fútbol 5", "Fútbol 7", "Fútbol 11", "Otro"])
ancho = st.number_input("Ancho (m)", min_value=1.0, step=0.5)
largo = st.number_input("Largo (m)", min_value=1.0, step=0.5)

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

rollo_ancho = st.radio("Ancho de rollo:", [2, 4])

# Cálculo si hay medidas
if ancho and largo:
    m2 = ancho * largo
    rollos = int(np.ceil(ancho / rollo_ancho) * np.ceil(largo / 25))
    total_pasto = m2 * precio_pasto

    # Accesorios
    arco = st.checkbox("Arcos (x2)")
    malla = st.checkbox("Malla perimetral")
    pintura = st.checkbox("Pintura de demarcación")

    total_accesorios = 0
    if arco: total_accesorios += 120000
    if malla: total_accesorios += m2 * 500
    if pintura: total_accesorios += 25000

    total_final = total_pasto + total_accesorios

    # Vista previa de la cancha
    fig_w, fig_h = largo * 0.15, ancho * 0.15
    fig, ax = plt.subplots(figsize=(fig_w, fig_h))
    ax.set_xlim(0, largo)
    ax.set_ylim(0, ancho)
    ax.set_aspect('equal')

    # Fondo
    ax.add_patch(patches.Rectangle((0, 0), largo, ancho, facecolor='green'))

    # Perímetro
    ax.plot([0, largo], [0, 0], color='white', lw=2)
    ax.plot([0, largo], [ancho, ancho], color='white', lw=2)
    ax.plot([0, 0], [0, ancho], color='white', lw=2)
    ax.plot([largo, largo], [0, ancho], color='white', lw=2)

    # Línea media y círculo
    ax.plot([largo/2, largo/2], [0, ancho], color='white', lw=2)
    ax.add_patch(patches.Circle((largo/2, ancho/2), radius=3, fill=False, edgecolor='white', lw=2))

    # Arcos básicos
    ax.add_patch(patches.Rectangle((0, ancho/2 - 3), 5, 6, fill=False, edgecolor='white', lw=2))
    ax.add_patch(patches.Rectangle((largo - 5, ancho/2 - 3), 5, 6, fill=False, edgecolor='white', lw=2))

    # Puntos de penal
    ax.plot([6], [ancho/2], 'wo')
    ax.plot([largo - 6], [ancho/2], 'wo')

    ax.set_title("Vista previa de la cancha")
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
