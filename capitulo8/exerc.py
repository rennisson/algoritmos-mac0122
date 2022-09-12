TESTE = ['ahlip', 'ala', 'sala', 'salas', '“socorrammesubinoonibusemmarrocos"']
ESPERADO = [False, True, False, True, True]

def main():
    n = len(TESTE)
    for t in range(n):
        s = TESTE[t]
        r = ESPERADO[t]
        print(f'{s}: devolveu {palindromo(s)} e deve ser {r}')


def palindromo(s):
    '''(str) -> bool
    Recebe uma string e verifica se é ou nao um palíndromo.
    '''
    

class Pilha:
    def __init__(self):
        ''' (Pilha) -> None
        Inicializa um objeto da classe Pilha.
        '''
        self.dados == []

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