import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Dimensiones reglamentarias FIFA
largo = 105
ancho = 68

# Crear figura con espacio para márgenes
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(-5, largo + 5)
ax.set_ylim(-5, ancho + 10)
ax.set_aspect('equal')

# Fondo total
ax.add_patch(patches.Rectangle((-5, -5), largo + 10, ancho + 15, color='#8BC34A'))

# Franjas alternadas (14 zonas)
for i in range(14):
    color = '#AED581' if i % 2 == 0 else '#9CCC65'
    ax.add_patch(patches.Rectangle((i * largo / 14, 0), largo / 14, ancho, color=color))

# Líneas de campo
ax.plot([0, largo], [0, 0], color='white', lw=2)
ax.plot([0, largo], [ancho, ancho], color='white', lw=2)
ax.plot([0, 0], [0, ancho], color='white', lw=2)
ax.plot([largo, largo], [0, ancho], color='white', lw=2)
ax.plot([largo / 2, largo / 2], [0, ancho], color='white', lw=2)
ax.add_patch(patches.Circle((largo / 2, ancho / 2), 9.15, fill=False, edgecolor='white', lw=2))
ax.plot([largo / 2], [ancho / 2], 'wo')

# Áreas grandes y chicas
for x in [0, largo - 16.5]:
    ax.add_patch(patches.Rectangle((x, (ancho - 40.32) / 2), 16.5, 40.32, fill=False, edgecolor='white', lw=2))
for x in [0, largo - 5.5]:
    ax.add_patch(patches.Rectangle((x, (ancho - 18.32) / 2), 5.5, 18.32, fill=False, edgecolor='white', lw=2))

# Puntos y semicírculos de penal
ax.plot([11], [ancho / 2], 'wo')
ax.plot([largo - 11], [ancho / 2], 'wo')
ax.add_patch(patches.Arc((11, ancho / 2), 18.3, 18.3, theta1=308, theta2=52, edgecolor='white', lw=2))
ax.add_patch(patches.Arc((largo - 11, ancho / 2), 18.3, 18.3, theta1=128, theta2=232, edgecolor='white', lw=2))

# Esquinas (córners)
for x, y, theta in [(0, 0, 0), (0, ancho, 270), (largo, 0, 90), (largo, ancho, 180)]:
    arc = patches.Arc((x, y), 2, 2, theta1=theta, theta2=theta + 90, edgecolor='white', lw=1.5)
    ax.add_patch(arc)

# Texto superior: largo
ax.annotate("90m (min) - 120m (max)", xy=(largo / 2, ancho + 4.5), ha='center', fontsize=12, color='white', weight='bold')
ax.annotate("←", xy=(0, ancho + 4.5), ha='right', fontsize=16, color='white')
ax.annotate("→", xy=(largo, ancho + 4.5), ha='left', fontsize=16, color='white')

# Texto lateral: ancho
ax.annotate("45m (min)\n-\n90m (max)", xy=(largo + 4, ancho / 2), va='center', ha='center',
            fontsize=12, color='white', weight='bold', rotation=90)
ax.annotate("↑", xy=(largo + 4, ancho), ha='center', fontsize=16, color='white')
ax.annotate("↓", xy=(largo + 4, 0), ha='center', fontsize=16, color='white')

# Franja inferior azul con texto
ax.add_patch(patches.Rectangle((-5, -5), largo + 10, 5, color='#001f6b'))
ax.text(largo / 2, -2.5, "Dimensiones para una cancha de fútbol 11", ha='center', fontsize=13, color='white', weight='bold')

# Ocultar ejes
ax.axis('off')

# Mostrar
plt.show()
