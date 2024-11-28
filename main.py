from grafo import Grafo
from visualizacao import desenhar_grafo

def menu():
    print("Menu:")
    print("1. Adicionar Vértice")
    print("2. Adicionar Aresta")
    print("3. Adicionar Grafo em Lote")
    print("4. Visualizar Grafo")
    print("5. Exibir Ordem e Tamanho")
    print("6. Obter Adjacentes de um Vértice")
    print("7. Obter Grau de um Vértice")
    print("8. Encontrar Caminho Mínimo entre Dois Vértices")
    print("0. Sair")

def main():
    direcionado = input("O grafo é direcionado? (s/n): ").strip().lower() == 's'
    valorado = input("O grafo é valorado? (s/n): ").strip().lower() == 's'
    grafo = Grafo(direcionado=direcionado, valorado=valorado)
    
    while True:
        menu()
        escolha = input("Escolha uma opção: ").strip()
        
        if escolha == "1":
            vertice = input("Digite o nome do vértice: ")
            grafo.adicionar_vertice(vertice)
            print(f"Vértice '{vertice}' adicionado.")
        
        elif escolha == "2":
            origem = input("Vértice de origem: ")
            destino = input("Vértice de destino: ")
            peso = int(input("Peso da aresta: ")) if grafo.valorado else 1
            grafo.adicionar_aresta(origem, destino, peso)
            print(f"Aresta de '{origem}' para '{destino}' adicionada.")
        
        elif escolha == "3":
            entrada = input("Digite os vértices e arestas no formato 'vértices; arestas': ")
            vertices_str, arestas_str = entrada.split(';')
            
            # Extrair vértices
            vertices = vertices_str.strip().split()
            
            # Extrair arestas
            arestas = []
            arestas_tokens = arestas_str.strip().split()
            i = 0
            while i < len(arestas_tokens):
                origem = arestas_tokens[i]
                destino = arestas_tokens[i + 1]
                peso = int(arestas_tokens[i + 2]) if grafo.valorado and i + 2 < len(arestas_tokens) else 1
                arestas.append((origem, destino, peso))
                i += 3 if grafo.valorado else 2
            
            grafo.adicionar_grafo_em_lote(vertices, arestas)
            print("Grafo em lote adicionado com sucesso.")
        
        elif escolha == "4":
            desenhar_grafo(grafo)
        
        elif escolha == "5":
            print(f"Ordem: {grafo.obter_ordem()}, Tamanho: {grafo.obter_tamanho()}")
        
        elif escolha == "6":
            vertice = input("Digite o vértice: ")
            adjacentes = grafo.obter_adjacentes(vertice)
            print(f"Adjacentes de '{vertice}': {adjacentes}")
        
        elif escolha == "7":
            vertice = input("Digite o vértice: ")
            grau = grafo.obter_grau(vertice)
            print(f"Grau de '{vertice}': {grau}")
        
        elif escolha == "8":
            origem = input("Digite o vértice de origem: ")
            destino = input("Digite o vértice de destino: ")
            distancia = grafo.caminho_minimo(origem, destino)
            print(f"Caminho mínimo de '{origem}' para '{destino}': {distancia}")
        
        elif escolha == "0":
            print("Encerrando...")
            break
        
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
