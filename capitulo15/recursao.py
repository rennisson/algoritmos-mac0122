TAB = '  '
def hanoi(n, origem, auxiliar, destino):
    '''(int, str, str, str) -> None
    Recebe o numero de discos n, os apelidos origem, auxiliar e destino dos pinos.
    Imprime as messagens com os movimentos para resolver o quebra-cabeça das Torres de Hanoi
        para movimentar n discos do pino origem para o pino destino usando o pino auxiliar.
    '''
    if n == 0: return None
    hanoi(n-1, origem, destino, auxiliar)
    print(f"mova o disco {n} do pino {origem} para o pino {destino}")
    hanoi(n-1, auxiliar, origem, destino)


def fatorialR(n, nivel=0):
    '''(int) -> int
    Recebe um inteiro n.
    Retorna n!.
    '''
    # caso base
    if n == 0:
        print(f'{TAB * nivel} fatorialR({n}) = {1}')
        return 1
    else:
        print(f'{TAB * nivel} fatorialR({n})')
        result = fatorialR(n - 1, nivel + 1) * n
        print(f'{TAB * nivel} fatorialR({n}) = {result}')
        return result


def regua(n, lista=[]):
    # lista = []
    # if n % 2 == 0:
    #     lista = (n ** 2 - 1) * []
    # else:
    #     lista = (n ** 2 - 2) * []
    if n == 2:
        lista.append(n-1)
        lista.append(n)
        lista.append(n-1)
        #print(lista)
        return lista

    return regua(n - 1, lista)

regua(3)