# Pacote auxiliar para o cálculo do tempo
from time import time
import BFS
import puzzle
import numpy as np
import json

# 362.880 combinations
# Criando objeto do problema
problema = puzzle.SlidingPuzzle(3)
# arquivo = input('Entre com o nome do aquivo: ')
# Criando Matriz inicial e matriz alvo

with open("puzzle_dados.json", encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

target = np.matrix(
  dados['objetivo']
)

start = np.matrix(
    dados['start']
)

# Mostrando informações iniciais
print(f"Initial state: \n{start}")
print("*"*15)
print(f"Target state: \n{target}")
print("*"*15)



# Execução do BFS
bfs = BFS.BreadthFirstSearch(problema)

ini = time() # Tempo inicial

bfs_solucao, bfs_estados_visitados, bfs_num_visitados = bfs.busca(start, target) # chamando busca

bfs_time = time()-ini # Tempo total

if bfs_solucao:
    print(f"Solution found!!!")
else:
    print("Solution not found!!!")

print(f'tempo: {bfs_time}')
