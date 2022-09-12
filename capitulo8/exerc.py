TESTE_PALINDROMO = ['ahlip', 'ala', 'sala', 'salas', 'socorrammesubinoonibusemmarrocos']
ESPERADO_PALINDROMO = [False, True, False, True, True]
TESTE_FORMAT = ['()[] ([])', '([)]', '()(', ']()[']
ESPERADO_FORMAT = [True, False, False, False]

def main():
    n = len(TESTE_PALINDROMO)
    for t in range(n):
        s = TESTE_PALINDROMO[t]
        r = ESPERADO_PALINDROMO[t]
        print(f'{s}: devolveu {palindromo(s)} e deve ser {r}')

    print("\n \n")
    for i in range(len(TESTE_FORMAT)):
        s = TESTE_FORMAT[i]
        r = ESPERADO_FORMAT[i]
        print(f'"{s}": devolveu {bem_formatada(s)} e deve ser {r}')


def palindromo(s):
    '''(str) -> bool
    Recebe uma string e verifica se é ou nao um palíndromo.
    '''
    pilha = Pilha()

    # Empilhando os caracteres de S em 'pilha'
    for i in range(len(s)):
        pilha.empilhe(s[i])

    str = ''
    # Desempilhando os caracteres de 'pilha' e guardando em 'str'
    for i in range(len(pilha)):
        str += pilha.desempilhe()

    # Se 's' for igual a 'str', retorna True
    # Se não, retorna False
    return s == str


def bem_formatada(s):
    '''(str) -> bool
    Recebe uma string e verifica se está bem formatada ou não
    '''
    # Se o primeiro caractere for ) ou ], retorna False.
    if s[0] in ')]':
        return False

    pilha = []
    for i in range(len(s)):
        if s[i] in '([':
            pilha.append(s[i])

        if (s[i] == ')' and pilha[-1] == '(') or (s[i] == ']' and pilha[-1] == '['):
            pilha.pop()

    if pilha == []:
        return True
    return False


class Pilha:
    def __init__(self):
        ''' (Pilha) -> None
        Inicializa um objeto da classe Pilha.
        '''
        self.dados = []

    def __len__(self):
        '''(Pilha) -> int
        Recebe um objeto Pilha e retorna o seu tamanho
        '''
        return len(self.dados)

    def vazia(self):
        ''' (Pilha) -> bool
        Recebe um objeto Pilha e retorna True se estiver vazio. Se não, retorna False.
        '''
        return self.dados == []

    def empilhe(self, item):
        '''(Pilha, item) -> None
        Recebe um objeto Pilha e um item, e adiciona este item no topo de Pilha
        '''
        self.dados.append(item)

    def desempilhe(self):
        '''(Pilha) -> objeto
        Recebe um objeto Pilha e desempilha e retorna o objeto no topo da Pilha
        '''
        return self.dados.pop()

    def topo(self):
        '''(Pilha) -> objeto
        Recebe um objeto Pilha e retorna o objeto no topo da Pilha.
        Não remove o objeto da Pilha.
        '''
        return self.dados[-1]


if __name__ == '__main__':
    main()