from grafo.grafo import Grafo
from algoritmos.AEstrela import AEstrela

def main():
    grafo = Grafo()

    aestrela = AEstrela(grafo.curitiba) #O destino é sempre Bucharest
    aestrela.buscar(grafo.saoMateusDoSul) #Insira aqui a cidade inicial

if __name__ == "__main__":
    main()