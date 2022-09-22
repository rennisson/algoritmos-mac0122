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

## enquanto um import carrega todo o módulo,
## o uso de from permite importar apenas a classe Array2D
from array2d import Array2D, flipH


## ==================================================================

def main():
    print("Testes da classe Array2D\n")

    a = Array2D((1, 6), 3)  # cria Array2D com valor inicial 3
    print(f'teste 1: Criação do Array2D a:')
    print(a)

    b = a.reshape((2, 3))
    print(f'\nteste 2: reshape cria uma vista b = a.reshape')
    print(b)

    print(f'\nteste 3: mudanças em b devem resultar em mudanças em a:')
    b[1, 2] = 100
    print(a)
    print()
    print(b)

    print(f'\nteste 4: e vice-versa - mudanças em a devem resultar em mudanças em b:')
    a[0, 2] = -1
    print(a)
    print()
    print(b)

    print(f'\nteste 5: copy cria um clone')
    a = Array2D((1, 6), 3)  # cria Array2D com valor inicial 3
    c = a.copy()
    print(f'a: {a}')
    print()
    print(f'c: {c}')

    print(f'\nteste 6: mudanças em um objeto não devem refletir no outro')
    a[0, 1] = 99
    c[0, 5] = -1
    print(f'a: {a}')
    print()
    print(f'c: {c}')

    print('>>> Testes carregue_copia() e carregue_vista() \n')

    lista = [1, 2, 3, 4, 5, 6]
    ac = Array2D((2, 3), 0)
    av = Array2D((2, 3), 0)

    ac.carregue_copia(lista)
    av.carregue_vista(lista)
    print(f'ac:\n{ac}\n')
    print(f'av:\n{av}\n')
    print(f'lista: {lista}')
    print()

    av[1, 1] = -1
    print(f'ac:\n{ac}\n')
    print(f'av:\n{av}\n')
    print(f'lista: {lista}')
    print()

    ac[0, 2] = -2
    print(f'ac:\n{ac}\n')
    print(f'av:\n{av}\n')
    print(f'lista: {lista}\n')

    print('>>> Testes flipV() e flipH() \n')

    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    a = Array2D((2, 5), 0)
    a.carregue_vista(lista)
    print(f'a:\n{a}\n')

    flipV = a.flipV()
    print(f'flipV:\n{flipV}\n')

    print(f'a:\n{a}\n')
    print(f'lista: {lista}\n')

    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    a = Array2D((2, 5), 0)
    a.carregue_vista(lista)
    print(f'a:\n{a}\n')

    flipH(a)
    print(f'a depois de flipH:\n{a}\n')
    print(f'lista: {lista}')


## ==================================================================


## ==================================================================

if __name__ == '__main__':
    main()