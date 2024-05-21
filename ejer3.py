# -*- coding: utf-8 -*-
"""
Created on Sun May 12 20:11:34 2024

@author: ddiaz
"""

import networkx as nx
import matplotlib.pyplot as plt

# Creamos un grafo dirigido
# Creamos un grafo dirigido
G = nx.DiGraph()

# Añadimos los nodos
nodos = ["Bartolome", "Julia", "Ninet", "Patricia", "Vidal", "Jhanet", "Daniel", "Josue", "Samuel", "Fernando"]
G.add_nodes_from(nodos)

# Añadimos las aristas con las relaciones familiares
relaciones = [("Bartolome", "Patricia"), ("Bartolome", "Jhanet"), ("Bartolome", "Ninet"),
              ("Julia", "Ninet"), ("Julia", "Jhanet"), ("Julia", "Patricia"),
              ("Jhanet", "Daniel"), ("Vidal", "Daniel"), ("Vidal", "Samuel"),
              ("Vidal", "Josue"), ("Jhanet", "Samuel"), ("Jhanet", "Josue"),
              ("Patricia", "Fernando")]
G.add_edges_from(relaciones)

# Visualizamos el grafo
plt.figure(figsize=(10, 6))  # Tamaño del lienzo
pos = nx.spring_layout(G, seed=42)  # Posiciones de los nodos
nx.draw_networkx_nodes(G, pos, node_size=2000, node_color="lightblue", alpha=0.8)
nx.draw_networkx_edges(G, pos, width=2, edge_color="gray", arrowsize=20)
nx.draw_networkx_labels(G, pos, font_size=12, font_family="sans-serif")
plt.title("Relaciones Familiares", fontsize=16)
plt.axis("off")  # Apagamos los ejes
plt.tight_layout()
plt.show()

