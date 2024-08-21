from grafo.grafo import Grafo
from algoritmos.AEstrela import AEstrela

def main():
    grafo = Grafo()

    aestrela = AEstrela(grafo.bucharest) #O destino é sempre Bucharest
    aestrela.buscar(grafo.timisoara) #Insira aqui a cidade inicial

if __name__ == "__main__":
    main()