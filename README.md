# Dijkstras-Algorithm

### Rutas Turísticas en Antigua Guatemala

Este proyecto implementa el **algoritmo de Dijkstra** para encontrar rutas óptimas entre puntos turísticos en Antigua Guatemala. Permite la **visualización de rutas** en un grafo que representa las calles de la ciudad y soporta varias opciones de recorrido.

## Características

- Calcular la **ruta más corta** entre dos puntos.
- Calcular rutas con **una parada intermedia**.
- Calcular rutas **evitando obstáculos**.
- Calcular rutas considerando **condiciones de tráfico**.
- Visualizar rutas usando **Matplotlib**.
- Menú interactivo para seleccionar puntos de inicio, parada y destino.

## Requisitos

Python 3.x con las siguientes librerías:

```bash
pip install requests pandas networkx matplotlib
```

### Usar el menú interactivo para seleccionar opciones de ruta:

- Ruta simple (inicio → fin)
- Ruta con parada intermedia
- Ruta evitando un obstáculo
- Ruta considerando tráfico

### Visualización

Los nodos y aristas se colorean para identificar: Las rutas se muestran usando Matplotlib.

- Inicio: rojo
- Destino: verde
- Camino óptimo: amarillo
- Puntos turísticos (checkpoints): gris
- Otros nodos: negro
