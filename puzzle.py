import numpy as np


class SlidingPuzzle():
    def __init__(self, num_blocos):
        '''
        Construtor
        Args:
            - num_blocos: numero de blocos por linha e coluna, valor inteiro (Ex: 3 significa 3 linhas e 3 colunas)
        '''
        self.num_blocos = num_blocos

    def _encontra_posicao(self, estado, elemento):
        '''
        Varre todo o tabuleiro (estado) e verifica em qual posição 'elemento' está
        Args:
            - estado: matriz contendo o estado do tabuleiro
            - elemento: elemento a ser buscado na matriz
        Return:
            - Retorna a linha e coluna onde o elemento se encontra
        '''
        for i in range(self.num_blocos):
            for j in range(self.num_blocos):
                if estado[i, j] == elemento:
                    return i, j
        return None, None

    def verifica_estados(self, atual, objetivo):
        '''
        Verifica se dois estados são iguais
        Args:
            - atual: matriz que descreve o estado atual
            - objetivo: matriz que descreve o estado objetivo
        Return:
            - booleano dizendo se o estado atual é ou não o objetivo
        '''
        flag = True
        for i in range(self.num_blocos):
            for j in range(self.num_blocos):
                if atual[i, j] != objetivo[i, j]:
                    flag = False
                    break

        return flag

    def expande_estados(self, atual):
        '''
        Dado o estado atual, realiza a expansão de estados
        Args:
            - atual: matriz que descreve o estado atual
        Return:
            - lista com os novos estados após a expansão
        '''

        novos_estados = []
        linha, coluna = self._encontra_posicao(atual, 0)

        # Cima
        if linha > 0:
            novo_estado = np.copy(atual)
            nova_linha = linha - 1

            bloco_alvo = novo_estado[nova_linha, coluna]
            novo_estado[nova_linha, coluna] = 0
            novo_estado[linha, coluna] = bloco_alvo

            novos_estados.append(novo_estado)

        # Baixo
        if linha < self.num_blocos - 1:
            novo_estado = np.copy(atual)
            nova_linha = linha + 1

            bloco_alvo = novo_estado[nova_linha, coluna]
            novo_estado[nova_linha, coluna] = 0
            novo_estado[linha, coluna] = bloco_alvo

            novos_estados.append(novo_estado)

        # Esquerda
        if coluna > 0:
            novo_estado = np.copy(atual)
            nova_coluna = coluna - 1

            bloco_alvo = novo_estado[linha, nova_coluna]
            novo_estado[linha, nova_coluna] = 0
            novo_estado[linha, coluna] = bloco_alvo

            novos_estados.append(novo_estado)

        # Direita
        if coluna < self.num_blocos - 1:
            novo_estado = np.copy(atual)
            nova_coluna = coluna + 1

            bloco_alvo = novo_estado[linha, nova_coluna]
            novo_estado[linha, nova_coluna] = 0
            novo_estado[linha, coluna] = bloco_alvo

            novos_estados.append(novo_estado)

        return novos_estados
