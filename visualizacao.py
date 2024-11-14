import networkx as nx
import matplotlib.pyplot as plt

def desenhar_grafo(grafo):
    G = nx.DiGraph() if grafo.direcionado else nx.Graph()
    for vertice in grafo.vertices:
        G.add_node(vertice)
    for (origem, destino), peso in grafo.arestas.items():
        G.add_edge(origem, destino, weight=peso)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight="bold")
    labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show(block=False)
