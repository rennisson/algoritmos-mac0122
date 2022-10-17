def main():
    print('-------- testes fibonacciRM() --------')
    print(f'{fibonacciRM(0) = }')
    print(f'{fibonacciRM(1) = }')
    print(f'{fibonacciRM(2) = }')
    print(f'{fibonacciRM(3) = }')
    print(f'{fibonacciRM(4) = }')
    print(f'{fibonacciRM(5) = }')
    print(f'{fibonacciRM(6) = }')
    print(f'{fibonacciRM(7) = }')
    print(f'{fibonacciRM(8) = }')
    print(f'{fibonacciRM(9) = }')
    print(f'{fibonacciRM(10) = }')
    print(f'{fibonacciRM(20) = }')
    print(f'{fibonacciRM(30) = }')
    print(f'{fibonacciRM(40) = }')
    print(f'{fibonacciRM(50) = }')

def fibonacciRM(n):
    '''(int) -> int
    envoltória para fibonacciRCache().
    '''
    # -1 indica que o valor correspondente a posição não foi calculado
    cache = [-1]*(n+1)
    return fibonacciRCache(n, cache)


def fibonacciRCache(n, cache, soma=0):
    '''(int) -> int
    RECEBE um inteiro não negativos n.
    RETORNA o n-ésimo número de Fibonacci.
    '''
    # BASE
    # se FinonacciR(n) está no cache, retorne seu valor
    cache[0] = 0
    if cache[n] > -1: return cache[n]
    elif n < 2: cache[n] = n
    else:
        # REDUZA: se Finonacci(n) não está no cache, calcule-o recursivamente
        cache[n-1], soma = fibonacciRCache(n-1, cache, soma)
        # cache[n-2] = fibonacciRCache(n-2, cache) # Supérflua. Por quê?

        # RESOLVA: calcule Fibonacci(n)
        cache[n] = cache[n-2] + cache[n-1]
        soma += 1
    return cache[n], soma

main()