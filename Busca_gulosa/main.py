from grafo.grafo import Grafo
from algoritmos.gulosa import Gulosa

def main():
    grafo = Grafo()

    busca_gulosa = Gulosa(grafo.bucharest) #O destino é sempre Bucharest
    busca_gulosa.buscar(grafo.timisoara) #Insira aqui a cidade inicial

if __name__ == "__main__":
    main()