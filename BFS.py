from queue import Queue
import json

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
        with open("puzzle_dados.json", encoding='utf-8') as meu_json:
            dados = json.load(meu_json)
        fila = Queue()
        fila.put(inicio)

        solucao_encontrada = False
        estados_visitados = []
        cont_estados = 0
        qtd_nos = 0

        while not fila.empty():
            atual = fila.get()
            estados_visitados.append(atual)

            if self.problema.verifica_estados(atual, fim):
                solucao_encontrada = True
                break

            else:
                cont_estados += 1
                print(f"Visitando #{cont_estados}")
                novos_estados = self.problema.expande_estados(atual)
                if qtd_nos <= 362880:
                    for i in novos_estados:
                        if not self._verifica_visitado(i, estados_visitados):
                            fila.put(i)
                            qtd_nos += 1
                            print(f'nó [{qtd_nos}]')
                            print(i)
                            if qtd_nos % 500 == 0:
                                li = list(fila.queue)
                                dados['fila']
                                print('dados')
                                print(dados['fila'])


        return solucao_encontrada, estados_visitados, cont_estados