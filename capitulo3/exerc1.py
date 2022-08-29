def main():
    print(f'TESTE 1 -> {[5, 0, 7, -3, 9]}')
    res = minimo([5, 0, 7, -3, 9])
    print(f'O menor valor é {res[0]} e o seu índice é {res[1]}')

    print(f'TESTE 2 -> {[-5, 2, 1, -4, 10]}')
    res = minimo([-5, 2, 1, -4, 10])
    print(f'O menor valor é {res[0]} e o seu índice é {res[1]}')


def minimo(lista):
    valor_min = 0
    index = 0
    for i in range(len(lista)):
        if lista[i] <= valor_min:
            valor_min = lista[i]
            index = i
    return valor_min, index


main()