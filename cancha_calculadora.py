import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Dimensiones reglamentarias
largo = 105  # en metros
ancho = 68   # en metros

# Crear figura con proporción real
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(0, largo)
ax.set_ylim(0, ancho)
ax.set_aspect('equal')

# Fondo con franjas alternadas (14 zonas)
for i in range(14):
    color = '#4CAF50' if i % 2 == 0 else '#43A047'
    ax.add_patch(patches.Rectangle((i * largo / 14, 0), largo / 14, ancho, color=color))

# Líneas perimetrales
ax.plot([0, largo], [0, 0], color='white', lw=2)
ax.plot([0, largo], [ancho, ancho], color='white', lw=2)
ax.plot([0, 0], [0, ancho], color='white', lw=2)
ax.plot([largo, largo], [0, ancho], color='white', lw=2)

# Línea media y círculo central
ax.plot([largo / 2, largo / 2], [0, ancho], color='white', lw=2)
ax.add_patch(patches.Circle((largo / 2, ancho / 2), 9.15, fill=False, edgecolor='white', lw=2))
ax.plot([largo / 2], [ancho / 2], 'wo')  # punto central

# Áreas grandes
for x in [0, largo - 16.5]:
    ax.add_patch(patches.Rectangle((x, (ancho - 40.32) / 2), 16.5, 40.32, fill=False, edgecolor='white', lw=2))

# Áreas chicas
for x in [0, largo - 5.5]:
    ax.add_patch(patches.Rectangle((x, (ancho - 18.32) / 2), 5.5, 18.32, fill=False, edgecolor='white', lw=2))

# Puntos penales
ax.plot([11], [ancho / 2], 'wo')             # lado izquierdo
ax.plot([largo - 11], [ancho / 2], 'wo')      # lado derecho

# Arcos de penal (semicírculos)
ax.add_patch(patches.Arc((11, ancho / 2), 18.3, 18.3, theta1=308, theta2=52, edgecolor='white', lw=2))
ax.add_patch(patches.Arc((largo - 11, ancho / 2), 18.3, 18.3, theta1=128, theta2=232, edgecolor='white', lw=2))

# Córners (cuartos de círculo)
radio_esquina = 1
corners = [
    (0, 0, 0), (0, ancho, 270),
    (largo, 0, 90), (largo, ancho, 180)
]
for x, y, angle in corners:
    corner_arc = patches.Arc((x, y), 2 * radio_esquina, 2 * radio_esquina, angle=0, theta1=angle, theta2=angle + 90, edgecolor='white', lw=1.5)
    ax.add_patch(corner_arc)

# Título
ax.set_title("Dimensiones para una cancha de fútbol 11", fontsize=14)

# Quitar ejes
ax.axis('off')

# Mostrar
plt.show()
