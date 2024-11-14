class Grafo:
    def __init__(self, direcionado=False, valorado=False):
        self.direcionado = direcionado
        self.valorado = valorado
        self.vertices = {}
        self.arestas = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def adicionar_aresta(self, origem, destino, peso=1):
        if self.valorado:
            self.arestas[(origem, destino)] = peso
        else:
            self.arestas[(origem, destino)] = None
        if not self.direcionado:
            self.arestas[(destino, origem)] = peso if self.valorado else None
        self.vertices[origem].append(destino)
        if not self.direcionado:
            self.vertices[destino].append(origem)

    def obter_ordem(self):
        return len(self.vertices)

    def obter_tamanho(self):
        return len(self.arestas) // (2 if not self.direcionado else 1)

    def obter_adjacentes(self, vertice):
        return self.vertices.get(vertice, [])
    
    def obter_grau(self, vertice):
        grau_saida = len(self.obter_adjacentes(vertice))
        grau_entrada = len([origem for origem, _ in self.arestas if _ == vertice])
        return (grau_entrada, grau_saida) if self.direcionado else grau_saida

    def caminho_minimo(self, origem, destino):
        import heapq
        dist = {v: float('inf') for v in self.vertices}
        dist[origem] = 0
        pq = [(0, origem)]
        while pq:
            (custo, atual) = heapq.heappop(pq)
            if atual == destino:
                break
            for vizinho in self.vertices[atual]:
                peso = self.arestas[(atual, vizinho)] if self.valorado else 1
                if custo + peso < dist[vizinho]:
                    dist[vizinho] = custo + peso
                    heapq.heappush(pq, (dist[vizinho], vizinho))
        return dist[destino] if dist[destino] != float('inf') else None
