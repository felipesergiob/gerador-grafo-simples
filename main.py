from grafo import Grafo
from visualizacao import desenhar_grafo

def menu():
    print("Menu:")
    print("1. Adicionar Vértice")
    print("2. Adicionar Aresta")
    print("3. Visualizar Grafo")
    print("4. Exibir Ordem e Tamanho")
    print("5. Obter Adjacentes de um Vértice")
    print("6. Obter Grau de um Vértice")
    print("7. Encontrar Caminho Mínimo entre Dois Vértices")
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
            print(f"Aresta de '{origem}' para '{destino}' com peso {peso} adicionada.")
        
        elif escolha == "3":
            desenhar_grafo(grafo)
        
        elif escolha == "4":
            print(f"Ordem: {grafo.obter_ordem()}, Tamanho: {grafo.obter_tamanho()}")
        
        elif escolha == "5":
            vertice = input("Digite o vértice: ")
            adjacentes = grafo.obter_adjacentes(vertice)
            print(f"Adjacentes de '{vertice}': {adjacentes}")
        
        elif escolha == "6":
            vertice = input("Digite o vértice: ")
            grau = grafo.obter_grau(vertice)
            print(f"Grau de '{vertice}': {grau}")
        
        elif escolha == "7":
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
