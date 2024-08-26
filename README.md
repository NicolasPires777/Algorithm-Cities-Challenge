# IA-Cities-Challenge

![Mapa da Romênia](/Busca_gulosa/static/cities.png)

O desafio apresenta dois algoritmos, um com conceitos de busca gulosa e outro com busca A*.Ambos para partir de uma cidade qualquer e passar pelo caminho mais curto até Bucharest

O algoritmo com Busca Gulosa considera distância em linha reta até o destino para escolher sua próxima parada, por isso, em alguns momentos ele pode tomar decisões precipitadas.

Já o Algoritmo com Busca A* considera tanto a distância em linha reta quanto a distância por estrada até a próxima parada, trazendo mais precisão.


## Como testar?

1. Faça um clone do repositório para seu computador
2. Crie um ambiente virtual com o módulo "venv" do python ("python -m venv nome-do-ambiente")
3. Ative o ambiente virtual 
    - Para linux: "source ./nome-do-ambiente/Scripts/activate"
    - Para windows: ".\nome-do-ambiente\Scripts\activate
4. Baixe as dependencias: "pip install -r requirements.txt"
5. Testar algoritmo de Busca gulosa:
    1. No arquivo "./Busca_gulosa/main.py", na linha 8, selecione a cidade de partida. (O destino é sempre Curitiba!)
    2. Rode o código: "python ./Busca_gulosa/main.py"
6. Testar algoritmo de busca A*:
    1. No arquivo "./A estrela/main.py", na linha 8, selecione a cidade de partida. (O destino é sempre Curitiba!)
    2. Rode o código: "python ./A estrela/main.py"