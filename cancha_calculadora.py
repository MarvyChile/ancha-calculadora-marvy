
import streamlit as st
import matplotlib.pyplot as plt
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

# Modelo de pasto
st.markdown("### Modelo de pasto sintético")
modelo_pasto = st.selectbox(
    "Selecciona el modelo:",
    [
        "Basic 15mm - $5.040/m²",
        "Vivo 30mm - $8.900/m²",
        "Royal 40mm - $8.415/m² (Oferta)",
        "Prime 40mm - $10.900/m²"
    ]
)

# Ancho del rollo
rollo_seleccionado = st.radio("Selecciona el ancho del rollo:", [2, 4])

# Precios por modelo
precios = {
    "Basic 15mm - $5.040/m²": 5040,
    "Vivo 30mm - $8.900/m²": 8900,
    "Royal 40mm - $8.415/m² (Oferta)": 8415,
    "Prime 40mm - $10.900/m²": 10900
}

# Cálculos
if ancho and largo:
    m2 = ancho * largo
    total_pasto = m2 * precios[modelo_pasto]
    cantidad_rollos = int(np.ceil(ancho / rollo_seleccionado) * np.ceil(largo / 25))

    # Accesorios
    st.markdown("### Accesorios opcionales")
    arco = st.checkbox("Arcos (x2)", value=False)
    malla = st.checkbox("Malla perimetral", value=False)
    pintura = st.checkbox("Pintura demarcación", value=False)

    costo_accesorios = 0
    if arco:
        costo_accesorios += 120000
    if malla:
        costo_accesorios += m2 * 500
    if pintura:
        costo_accesorios += 25000

    total_final = total_pasto + costo_accesorios

    # Visualización gráfica
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.set_xlim(0, largo)
    ax.set_ylim(0, ancho)
    ax.set_aspect('equal')
    ax.add_patch(plt.Rectangle((0, 0), largo, ancho, facecolor='green', edgecolor='white'))
    ax.set_title("Vista previa de la cancha")
    ax.axis('off')
    st.pyplot(fig)

    # Resumen
    st.markdown("## 🧾 Resumen")
    st.markdown(f"- Tipo de cancha: **{tipo_cancha}**")
    st.markdown(f"- Modelo de pasto: **{modelo_pasto}**")
    st.markdown(f"- Superficie: **{m2:.2f} m²**")
    st.markdown(f"- Rollos de {rollo_seleccionado}m: **{cantidad_rollos}**")
    st.markdown(f"- Costo pasto: **${total_pasto:,.0f}**")
    st.markdown(f"- Costo accesorios: **${costo_accesorios:,.0f}**")
    st.markdown(f"### ✅ Total estimado: **${total_final:,.0f}**")
