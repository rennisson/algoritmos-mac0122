'''
O Jogo da Vida (The Game of Life) é um autômato celular (cellular automaton) introduzido por John Horton Conway em 1970.
Um automato celular consiste de uma rede de células. Cada célula pode estar em um número finito de estados, como
morta ou viva. O “jogo” é na verdade uma simulação que permite observar a evolução de um processo a partir de uma certa
condição inicial.

O jogo se desenvolve sobre uma matriz bi-dimensional que pode ser tão grande quanto se queira. Vamos chamar essa matriz
de mapa. Cada posição ou célula do mapa pode estar vazia (= célula morta) ou ocupada por um agente (= célula viva).
Cada posição possui também até 8 posições vizinhas: imediatamente acima, abaixo, aos lados e nas diagonais. Em um
determinado instante, o mapa contém uma geração de agentes. A geração no instante seguinte é determinada segundo as
regras abaixo:

se uma célula [i,j] está vazia então:
    um novo agente nasce em [i,j] se essa célula possui exatamente 3 agentes vizinhos;
se uma célula [i,j] possui um agente então:
    o agente em [i,j] sobrevive se possui 2 ou 3 agentes vizinhos;
    o agente em [i.j] morre se possuir menos de 2 agentes vizinhos, por falta de recursos;
    o agente em [i.j] morre se possuir mais de 3 agentes vizinhos, por excesso de competição.
'''

import numpy as np


def main():
    print(f'-----------------')
    a = [[0, 0], [0, 0]]
    ar = np.array(a)
    iteracao(ar)
    print(ar)

    print(f'-----------------')
    a = [[1, 0, 0], [1, 0, 0]]
    ar = np.array(a)
    iteracao(ar)
    print(ar)

    print(f'-----------------')
    a = [[1, 1, 0], [0, 1, 1]]
    ar = np.array(a)
    iteracao(ar)
    print(ar)

    print(f'-----------------')
    a = [[1, 1, 1], [1, 1, 1]]
    ar = np.array(a)
    iteracao(ar)
    print(ar)

    print(f'-----------------')
    a = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    ar = np.array(a)
    iteracao(ar)
    print(ar)

    print(f'-----------------')
    a = [[1, 1, 1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1]]
    ar = np.array(a)
    iteracao(ar)
    print(ar)


def iteracao(M):
    ''' (mapa) -> None
    Recebe uma mapa (ndarray) com a geração de agentes em um determinado
    instante e atualiza o mapa de tal forma que represente geração de
    agentes no instante seguinte.
    '''
    nlin, ncol = M.shape

    for i in range(nlin):
        for j in range(ncol):
            # Verificações para garantir a fatia correta do array
            if i == 0 and j == 0:
                vista = M[0:2, 0:2]
            elif i == 0 and j != 0:
                vista = M[0:2, j - 1:j + 2]
            elif i != 0 and j == 0:
                vista = M[i - 1:i + 2, 0:2]
            else:
                vista = M[i - 1:i + 2, j - 1:j + 2]

            # Se M[i,j] for nulo, um novo agente nasce em [i,j] se essa célula possui exatamente 3 agentes vizinhos
            # vista.sum() representa o número de agentes vivos ao redor da celula M[i,j]
            if (M[i, j] == 0) and (vista.sum() == 3):
                M[i, j] = 1

            # Se M[i,j] possui um agente vivo, o agente em [i,j] morre se possuir
            # mais que 2 (falta de recursos) ou menos que 3 (excesso de competição) agentes vizinhos;
            # vista.sum()-1 representa o número de agentes vivos ao redor da celula M[i,j] subtraindo o próprio M[i,j]
            elif not (2 <= vista.sum() - 1 <= 3):
                M[i, j] = 0
    return


if __name__ == '__main__':
    main()
