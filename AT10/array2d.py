# -*- coding: utf-8 -*-
'''
    Atividade 10 - métodos e funções de Array2D

    Indique o código do Grupo (deveria ser o mesmo da computador
    que você usou no CEC, como A, B, C etc.).

    GRUPO: A

    Liste a seguir os nomes completos dos membros do time que participaram dessa atividade presencialmente:

    - Caio Domiciano Pires dos Santos
    - Leonardo Heidi Almeida Murakami
    - Rennisson Davi D. Alves

'''


## nesse exercício, escreva os testes no arquivo separado main.py


# =================================================================

class Array2D:
    '''
    A classe Array2D permite a manipulação de 'matrizes' de duas
    dimensões. O exercício é utilizar uma lista linear, ao invés
    de uma lista aninhada, para armazenar os dados da matriz
    internamente.
    A lista linear deve ser um atributo de nome 'data'.
    '''

    # ---------------------------------------------------------------
    def __init__(self, shape, val=0):
        ''' (Array2D, tuple, obj) -> None
        Constrói um objeto do tipo Array2D com os atributos:
        data : lista onde os valores são armazenados
        shape: tupla que armazena as dimensões da matriz
        size : número total de elementos da matriz
        '''
        nl, nc = shape
        self.shape = shape
        self.dtype = type(val)
        self.size = nl * nc
        self.data = [val] * self.size

    # ---------------------------------------------------------------
    def __getitem__(self, key):
        ''' (Array2D, tupla) -> obj
        recebe uma tupla key contendo a posição (lin, col)
        e retorna o item nessa posição do Array2D self.

        Esse método é usado quando o objeto é chamado com
        uma tupla entre colchetes, como self[0,0].
        Exemplo:
        >>> a = Array2D( (2,3), -1)
        >>> a[1,1] + 100
        99
        >>> print( a[1,1] )
        -1
        '''
        lin, col = key
        nlin, ncol = self.shape
        return self.data[lin * ncol + col]

    # ---------------------------------------------------------------
    def __setitem__(self, key, valor):
        ''' (Array2D, tupla, obj) -> None
        recebe uma tupla key contendo a posição (lin, col)
        e um objeto valor e armazena o valor nessa posição
        do Array2D self.

        Esse método é usado para atribuir 'valor' na posição
        indicada pela tupla `key`, como self[0,0] = 0.
        Exemplo:
        >>> a = Array2D( (2,3), -1)
        >>> print( a[1,1] )
        -1
        >>> a[1,1] = 100
        >>> print( a[1,1] )
        100
        '''

        lin, col = key
        nlin, ncol = self.shape
        self.data[lin * ncol + col] = valor

    # ---------------------------------------------------------------
    def __str__(self):
        ''' (Array2D) -> None
        ao ser usada pela função print, exibe cada linha
        do Array2D em uma linha separada.
        '''
        s = ''
        nlin, ncol = self.shape
        for k in range(self.size):
            s += f"{self.data[k]} "
            if (k + 1) % ncol == 0:
                s += "\n"
        return s[:-1]  # remove último \n

    # ---------------------------------------------------------------
    # Escreva outros métodos e funções caso desejar

    def copy(self):
        ''' Array2D --> Array2D
        '''
        aux = Array2D(self.shape)
        aux.data = self.data[:]
        return aux

    def reshape(self, tupla):

        '''Array2D, tupla --> Array2D
        '''
        aux = Array2D(tupla)
        aux.data = self.data
        return aux

    def carregue_vista(self, lista):
        ''' (Array2D, list) -> None
        '''
        self.data = lista

    # ---------------------------------------------------------------

    def carregue_copia(self, lista):
        ''' (Array2D, list) -> None
        '''
        self.data = lista[:]

    def flipV(self):
        '''ARRAY2d --> Array2D
        '''
        s = []
        nlin, ncol = self.shape
        for i in range(self.size - ncol, -1, -ncol):
            for k in range(i, i + ncol):
                s.append(self.data[k])
        ar2d = Array2D(self.shape)
        ar2d.carregue_copia(s)

        return ar2d

    ## ==================================================================


def flipH(ar):
    ''' Array2D -> None
    '''
    s = []
    nlin, ncol = ar.shape
    for i in range(0, ar.size + 1, ncol):
        ar.data[i:i + ncol] = ar.data[i:i + ncol][::-1]
