# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def elvis():
    fname = 'elvis.jpg'
    image = mpimg.imread(fname)
    gray = np.array(image)[:,:,2] ## pega canal G da imagem RGB

    elvis = NPImagem( (), gray ) # transforma o array em uma NPImagem
    print("elvis.shape: ", elvis.shape)
    plt.gray()
    plt.imshow(elvis.data)
    #plt.show()

    fname = 'einstein.jpg'
    image = mpimg.imread(fname)
    gray = np.array(image)[:,:,2] ## pega canal G da imagem RGB

    einstein = NPImagem( (), gray)
    print("einstein.shape", einstein.shape)

    plt.imshow(einstein.data)
    #plt.show()

    elvis.paste(einstein.crop(0, 0, einstein.shape[0], einstein.shape[1]), 25, 330)
    plt.imshow(elvis.data)
    plt.show()

def main():
    ''' Testes da classe NPImagem
    '''

    lista = list(range(20))
    ar = np.array(lista).reshape(4, 5)
    img1 = NPImagem((0, 0), ar)
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

    # testes parte 2
    lista = list(range(30))
    ar = np.array(lista).reshape(5, 6)
    img1 = NPImagem((0, 0), ar)  #
    print(f"img1:\n{img1}")
    print(f"Shape de img1: {img1.shape}\n")

    img2 = NPImagem((3, 2), 100)
    img3 = img2.crop()  ## cria uma cópia
    img2[2, 1] = -10
    print(f"img2[1,2]={img2[2, 1]}")
    print(f"img2:\n{img2}\n")
    print(f"img3:\n{img3}\n")

    img1.pinte_retangulo(1, 2, 3, 5, 99)
    print(f"img1.pinte_retangulo(1,2,3,5,99):\n{img1}\n")

    img2.pinte_retangulo(-1, -2, 1, 2, 88)
    print(f"img2.pinte_retangulo(-1,-2,1,2,88):\n{img2}\n")

    img3.pinte_retangulo(1, 0, 3, 4, 77)
    print(f"img3.pinte_retangulo(1,0,3,4,77):\n{img3}\n")

    # testes parte 3
    img1.paste(img2, 1, 2)
    print(f"img1.paste(img2,1,2):\n{img1}\n")

    img1.paste(img3, 3, 5)
    print(f"img1.paste(img3,3,5):\n{img1}\n")

    img1.paste(img3, -1, -1)
    print(f"img1.paste(img3,-1,-1):\n{img1}\n")

    # Inclua abaixo outros testes que desejar

    lista = list(range(20))
    ar = np.array(lista).reshape(4, 5)
    img1 = NPImagem((0, 0), ar)
    img2 = NPImagem((4, 5), 1)

    lista = list(range(30))
    ar = np.array(lista).reshape(5, 6)
    img2 = NPImagem((0, 0), ar)
    print(f'\nimg1 = \n{img1}')
    print(f'\nimg2 = \n{img2}')

    print(f'\nimg1 + 10 = \n {10 + img1}')
    print(f'\nimg1 + img2 = \n {img1 + img2}')
    print(f'\nimg1 * 10 = \n {img1 * 10}')
    print(f'\nimg1 * img2 = \n {img1 * img2}')

    img1 = NPImagem((4, 5), 1)
    img2 = NPImagem((4, 5), 1)

    print(f'\nimg1 = \n{img1}')
    print(f'\nimg1 * 0.5 = \n {img1 * 0.5}')
    print(f'\nimg2 = \n{img2}')

    print(f'\nimg1.blend(img2) = \n {img1.blend(img2, 0.2)}')




# ===================================================================

class NPImagem():
    ''' Complete os métodos da classe NPImagem
    '''

    ### Parte I ---------------------------------------

    def __init__(self, key=(0, 0), val=0):
        ''' (NPImagem, shape, val) -> None '''
        if type(val) is np.ndarray:
            self.data = val
        else:
            self.data = np.full(key, val)
        self.shape = self.data.shape

    def __str__(self):
        ''' (NPImagem) -> str '''
        return str(self.data)

    def __getitem__(self, key):
        ''' (NPImagem, tuple) -> val '''
        return self.data[key]

    def __setitem__(self, key, val):
        ''' (NPImagem, tuple, val) -> None '''
        self.data[key] = val

    def __add__(self, other):
        ''' (NPImagem, NPImagem ou int ou float) -> NPImagem
        Quando recebe dois objetos NPImagem, retorna a soma, elemento-a-elemento,
        dos pixels de self e other.
        Quando other for int ou float, todos os elementos de self são adicionados de other.
        '''
        soma = self.crop()

        if type(other) is int or type(other) is float:
            soma[:,:] = soma[:,:] + other

        if type(other) is NPImagem:
                soma[:, :] += other.data[0:self.shape[0],0:self.shape[1]]

        return soma

    def __mul__(self, other):
        ''' (NPImagem, NPImagem ou int ou float) -> NPImagem
        Quando recebe dois objetos NPImagem, retorna a multiplicação, elemento-a-elemento,
        dos pixels de self e other.
        Quando other for int ou float, todos os elementos de self são multiplicados de other.
        '''
        mult = self.crop()

        if type(other) is int or type(other) is float:
            mult[:, :] = mult[:, :] * other

        if type(other) is NPImagem:
            mult[:, :] *= other.data[0:self.shape[0], 0:self.shape[1]]

        return mult

    def __radd__(self, other):
        return self + other

    def __rmul__(self, other):
        return self * other

    def crop(self, sup=0, esq=0, inf=None, dir=None):
        ''' (NPImagem, int, int, int, int) -> NPImagem
        Recorta uma região retangular da NPImagem. A região é definida pelos
        cantos superior-esquerdo (sup,esq) e inferior-direito (inf,dir) de
        um retângulo.

        Esse método cria e retorna uma NPImagem de dimensão
        (inf-sup) x (dir-esq), com conteúdo igual ao do retângulo
        (sup,esq)x(inf,dir).
        '''
        sup, esq, inf, dir = self.adjust_bounds(sup, esq, inf, dir)
        corte = self.data[sup:inf, esq:dir]
        return NPImagem(key=corte.shape, val=corte.copy())

    ### Parte II ---------------------------------------

    def pinte_retangulo(self, sup, esq, inf, dir, v=0):
        ''' (NPImagem, int, int, int, int, int) -> None
        Recebe 4 inteiros que definem o canto superior-esquerdo (sup, esq) e
        o canto inferior-direito (inf,dir) de uma região retangular com
        relação a posição (0,0) de self, ou seja, os cantos são "deslocamentos"
        em pixeis com relação à origem.
        Esse método pinta, com o valor v, os pixeis de self que tenham sobreposição com o retângulo (sup,esq)x(inf,dir).
        '''
        sup, esq, inf, dir = self.adjust_bounds(sup, esq, inf, dir)
        self.data[sup:inf, esq:dir] = v

    ### Parte III  ---------------------------------------

    def paste(self, other, sup, esq):
        '''(NPImagem, NPImagem, int, int) -> None
        Recebe um objeto NPImagem other e um par de inteiros (sup, esq)
        que indica um deslocamento em relação à origem de self (posição (0,0))
        onde a NPImagem other deve ser sobreposta sobre self. Observe que
        esse deslocamento pode ser negativo. Caso não existir sobreposição,
        a imagem self fica inalterada.
        '''

        v_corr_value = -sup if sup < 0 else 0
        h_corr_value = -esq if esq < 0 else 0
        inf = sup + other.shape[0]
        dir = esq + other.shape[1]
        sup, esq, inf, dir = self.adjust_bounds(sup, esq, inf, dir)
        for i, j in zip(range(sup, inf), range(v_corr_value, v_corr_value + inf - sup)):
            for k, l in zip(range(esq, dir), range(h_corr_value, h_corr_value + dir - esq)):
                self.data[i, k] = other.data[j, l]

    def blend(self, other, alfa=0.5):
        ''' (NPImagem, NPImagem, float) -> NPImagem
        Recebe duas NPImagens e retorna uma nova NPImagem que mistura essas
        imagens com peso alfa e (1-alfa) tal que o resultado seja:
        (self * alfa) + (other * (1-alfa))
        '''
        print(self*alfa)

        return (self*alfa) + (other*(1-alfa))

    def adjust_bounds(self, sup, esq, inf, dir):
        if sup < 0:
            sup = 0
        if esq < 0:
            esq = 0

        if inf is not None:
            if inf > self.shape[0]:
                inf = self.shape[0]

        if dir is not None:
            if dir > self.shape[1]:
                dir = self.shape[1]
        return sup, esq, inf, dir


if __name__ == '__main__':
    main()
    # elvis()
