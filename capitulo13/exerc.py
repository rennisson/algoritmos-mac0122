'''
'''

import numpy as np


def main():
    print(f'-----------------')
    lista = list(range(20))
    ar = np.array(lista).reshape(4, 5)
    img1 = NPImagem((0, 0), ar)  #
    print(f"img1:\n{img1}")
    print(f"Shape de img1: {img1.shape}\n")

    img2 = NPImagem((4, 3), 100)
    print(f"img2:\n{img2}")
    print(f"Shape de img2: {img2.shape}\n")

    img2[1, 2] = -10
    print(f"img2[1,2]={img2[1, 2]}")
    print(f"img2:\n{img2}\n")

    img3 = img2.crop()  ## cria uma cópia
    print(f"img3:\n{img3}\n")

    img4 = img1.crop(0, 1, 3, 4)
    print(f"img4:\n{img4}\n")

    img5 = NPImagem((3, 2))
    print(f"img5:\n{img5}\n")

    img6 = img1.crop(1, 2)
    print(f"img6:\n{img6}\n")


class NPImagem:

    def __init__(self, shape=(0,0), val = 0):
        ''' Construtor da classe NPImagem
        '''
        if type(val) is np.ndarray:
            self.data = val  ## compartilha dados com val
        else:
            self.data = np.full(shape, val)
        self.shape = self.data.shape

    def __str__(self):
        return str(self.data)

    def __getitem__(self, key=(0,0)):
        lin, col = key
        return self.data[lin, col]

    def __setitem__(self, key, value):
        lin, col = key
        self.data[lin, col] = value
        return

    def crop(self, sup=0, esq=0, inf=-1, dir=-1):
        if inf == -1:
            inf = self.shape[0]
        if dir == -1:
            dir = self.shape[1]

        imag = self.data[sup:inf, esq:dir]
        return imag



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
