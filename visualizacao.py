import networkx as nx
import matplotlib.pyplot as plt

def desenhar_grafo(grafo):
    plt.clf()

    G = nx.DiGraph() if grafo.direcionado else nx.Graph()

    for vertice in grafo.vertices:
        G.add_node(vertice)

    for (origem, destino), peso in grafo.arestas.items():
        if grafo.valorado:
            G.add_edge(origem, destino, weight=peso)
        else:
            G.add_edge(origem, destino)

    pos = nx.spring_layout(G)

    nx.draw(G, pos, with_labels=True, font_weight="bold", node_size=500, node_color='skyblue', font_size=12)

    if grafo.valorado:
        labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.draw()
    plt.show(block=False)
