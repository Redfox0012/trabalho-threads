# Pacote auxiliar para o cálculo do tempo
import sys
from time import time
import BFS
import puzzle
import numpy as np
import json

print('-' * 150)
print('BEM VINDO!')
print('Trabalho de C012-Sistemas Operacionais')
print('- Em aula vimos como funciona as threads em um SO,o Trabalho tem como objetivo utiliza-se de threads. \n'
      '- Utilizamos o código base de Buscas em Largura (matéria C210-Inteligencia Computacional)\n'
      '  O objetivo é salvar todos os processos já realizados e nós criados utilizando threads\n'
      '  para salvar em um json')
print('-' * 150)
print('     #### Puzzle 3x3 ####     ')
print('A Busca em Largura resolve o famoso puzzle 3x3 com espaço vazio (sinalizado com 0)')
print('Para mudar o start(estado inicial) e o objetivo(estado final) vá no json puzzle_dados.json')
print('-' * 150)
#MENU
print('\n'*2)
print('MENU')
print('1 - iniciar')
print('2 - continuar processo')
op = input('Entre com a opção: ')

# Criando objeto do problema
problema = puzzle.SlidingPuzzle(3)
bfs = BFS.BreadthFirstSearch(problema)
if op == '1':
    with open("puzzle_dados.json", encoding='utf-8') as meu_json:
        dados = json.load(meu_json)

    start = np.matrix(
        dados['start']
    )

if op == '2':
    with open("em_processo.json", encoding='utf-8') as meu_json:
        dados = json.load(meu_json)

    start = np.matrix(
        dados['fila'][0]
    )

target = np.matrix(
        dados['objetivo']
    )

print(f"Start: \n{start}")
print("*" * 15)
print(f"objetivo: \n{target}")
print("*" * 15)
#
ini = time() # Tempo inicial

bfs_solucao, bfs_estados_visitados, bfs_num_visitados = bfs.busca(start, target) # chamando busca

bfs_time = time()-ini # Tempo total

if bfs_solucao:
    print(f"Solution found!!!")
else:
    print("Solution not found!!!")

print(f'tempo: {bfs_time}')
sys.exit()

# 362.880