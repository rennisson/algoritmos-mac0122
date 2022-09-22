# CONSTANTES QUE VOCÊ PODE USAR CASO DESEJAR
ADD = '+'
SUB = '-'
MUL = '*'
DIV = '/'

def main():
    ''' Programa para teste da função polonesa
    '''
    exp = input("Digite uma expressão posfixa: ")
    print(f"{exp} = {polonesa(exp)}")

def polonesa( exp ):
    ''' (str) -> float
    calcula o valor de uma expressao polonesa
    '''
    itens = separe(exp)
    tamanho = len(itens)
    exp_polonesa = []

    for i in range(tamanho - 1):
        '''
        if itens == []:
            return exp_polonesa

        if itens[-1] in '+-*/':
            ## exp_polonesa.extend([itens[-2], itens[-1]])
            exp_polonesa.insert(0, itens[-2])
            exp_polonesa.append(itens[-1])
            itens.pop()
        else:
            exp_polonesa.append(itens[-1])
        itens.pop()
        '''

        if itens[i] in '+-*/':
            exp_polonesa.append(itens[i+1])
            exp_polonesa.append(itens[i])
        else:
            exp_polonesa.append(itens[i])

    return exp_polonesa


def separe(exp):
    '''(str) -> list
    Recebe uma string e quebra ela em uma lista
    '''
    s = exp.strip()  ## Apaga os espaços em branco das extremidades
    itens = s.split()  ## Quebra os operandos e operadores da expressão
    return itens

main()