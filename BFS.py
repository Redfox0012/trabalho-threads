import collections
import json
import threading
import time
import numpy as np


def autosave(nome, delay):
    while flag_thread:
        fila_aux = np.array(fila.copy())
        estados_visitados_aux = np.array(estados_visitados)
        print(f"salvando\n")
        with open("puzzle_dados.json", encoding='utf-8') as meu_json:
            dados = json.load(meu_json)
            dados['fila'] = fila_aux.tolist()
            dados['visitados'] = estados_visitados_aux.tolist()
            with open("em_processo.json", 'w') as f:
                json.dump(dados, f, indent=2)


        time.sleep(5)


class BreadthFirstSearch():
    def __init__(self, problema):
        '''
        Construtor
        Args:
            - problema: objeto do problema a ser solucionado
        '''
        self.problema = problema

    def _verifica_visitado(self, estado, estados_visitados):
        '''
        Verifica se 'estado' está na lista de estados visitados
        Args:
            - estado: estado qualquer do tabuleiro
            - estados_visitados: lista com todos os estados já visitados
        Return:
            - booleano dizendo se o estado foi visitado ou não
        '''
        for i in estados_visitados:
            if self.problema.verifica_estados(i, estado):
                return True
        return False



    def busca(self, inicio, fim):
        '''
        Realiza a busca BFS, armazenando os estados em uma FILA
        Args:
            - inicio: estado inicial do problema
            - fim: estado objetivo
        Return:
            - booleano se a solução foi encontrada, lista dos estados visitados, quantidade de estados visitados
        '''
        global fila
        global flag_thread
        global estados_visitados
        estados_visitados = []
        flag_thread = True
        fila = collections.deque()
        fila.append(inicio)
        saver1 = threading.Thread(target=autosave, args=('t1', 0))
        saver1.start()
        solucao_encontrada = False


        cont_estados = 0
        while fila:
            atual = fila[0]
            fila.popleft()
            estados_visitados.append(atual)

            if self.problema.verifica_estados(atual, fim):
                solucao_encontrada = True
                break

            else:
                cont_estados += 1
                print(f"Visitando #{cont_estados}")
                novos_estados = self.problema.expande_estados(atual)
                for i in novos_estados:
                    if not self._verifica_visitado(i, estados_visitados):
                        fila.append(i)
        flag_thread = False
        return solucao_encontrada, estados_visitados, cont_estados
