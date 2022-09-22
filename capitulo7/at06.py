# -*- coding: utf-8 -*-
'''
    Atividade 06 - classe Horario

    Indique o código do Grupo (deveria ser o mesmo da computador
    que você usou no CEC, como A, B, C etc.).

    GRUPO: A

    Liste a seguir os nomes completos dos membros do time que participaram dessa atividade presencialmente:

    - Rennisson Davi D. Alves
    - Caio Domiciano Pires dos Santos
    - Gabriel Rodrigues Franchin

'''


def main():
    ''' Testes da classe Horario
    '''
    print("Testes da classe Horario\n")
    print("Testes da classe Horario\n")

    t1 = Horario(8)
    print(f't1 = {t1} e deve ser 08:00:00')

    t2 = Horario(1, 40)
    print(f't2 = {t2} e deve ser 01:40:00')

    h1 = Horario(0, 40)
    h2 = Horario(0, 0, 30)
    print(h2)
    h3 = Horario(50)
    print(h1, h2, h3)
    hm = h_min([h1, h2, h3])
    print(hm)

    hora1 = transf_horario_segundos(Horario(23, 59, 59))
    print(hora1)
    hora1 = Horario(23, 59, 59)

    hora2 = transf_segundos_horario(3600)
    print(hora2)

    print(hora1 < hora2)

    t123 = Horario(1, 2, 3)
    print(f't123 = {t123} e deve ser 01:02:03')

    ti = t123 + 2
    print(f'ti = {ti} e deve ser 03:02:03')

    ti = ti - 1
    print(f'ti = {ti} e deve ser 02:02:03')

    ti = 10 - ti
    print(f'ti = {ti} e deve ser 07:57:57')

    tf = 2.5 + t123
    print(f'tf = {tf} e deve ser 03:32:03')

    tf = tf - 1.2345
    print(f'tf = {tf} e deve ser 02:17:59')

    h123 = Horario(1, 2, 3)
    h345 = Horario(3, 4, 5)
    print(h345 - h123)
    print(h123 + h345)
    print(h345 - 1)
    print(1 + h123)


class Horario:
    '''Classe utilizada para representar um horário.

    Um horário é representado por três números inteiros maiores ou iguais
    a zero, armazenados em um atributo do tipo lista e de nome 'dados'.

       * `dados[2]`: um número inteiro entre 0 e 23 que indica horas
       * `dados[1]`: um número inteiro entre 0 e 59 que indica minutos
       * `dados[0]`: um número inteiro entre 0 e 59 que indica segundos

    Essa classe deve permitir os "comportamentos" ilustrados no enunciado.
    '''

    def __init__(self, hora=0, minutos=0, segundos=0):
        ''' (int, int, int) -> None
        Chamado pelo construtor da classe.

        Recebe três parâmetros (hora, minutos e segundos) e os insere em uma lista de dados.
        '''
        if hora >= 24:
            # Caso o usuario digite um valor maior igual que 24 para as Horas,
            # convertermos o valor para um correspondente entre 0 e 24
            hora = hora % 24
        if minutos >= 60:
            # Caso o usuario digite um valor maior igual que 60 para os Minutos,
            # convertermos o valor para um correspondente entre 0 e 59
            minutos = minutos % 60
        if segundos >= 60:
            # Caso o usuario digite um valor maior igual que 60 para os Segundos,
            # convertermos o valor para um correspondente entre 0 e 59
            segundos = segundos % 60

        self.dados = [0, 0, 0]
        self.dados[0] = segundos
        self.dados[1] = minutos
        self.dados[2] = hora

    def __str__(self):
        ''' (Horario) -> str
        '''
        return f'{self.dados[2]:02}:{self.dados[1]:02}:{self.dados[0]:02}'

    def __add__(self, other):
        ''' (Horario, Horario) -> (Horario)
        Recebe dois parâmetros, self e other, e soma os dois Horarios.
        '''
        if type(other) is int or type(other) is float:
            other = Horario(other)

        self_seg = transf_horario_segundos(self)
        other_seg = transf_horario_segundos(other)

        novo_horario = transf_segundos_horario(self_seg + other_seg)

        return novo_horario

    def __radd__(self, other):
        ''' (Horario, Horario) -> (Horario) + (Horario)
        '''
        return self + other

    def __sub__(self, other):
        ''' (Horario, Horario) -> (Horario)
        Recebe dois parâmetros, self e other, e soma os dois Horarios.
        '''
        if type(other) is int or type(other) is float:
            other = Horario(other)

        self_seg = transf_horario_segundos(self)
        other_seg = transf_horario_segundos(other)

        if self > other:
            novo_horario = transf_segundos_horario(self_seg - other_seg)
        else:
            novo_horario = transf_segundos_horario(other_seg - self_seg)

        return novo_horario

    def __rsub__(self, other):
        ''' (Horario, Horario) -> (Horario) - (Horario)
        '''
        return self - other

    def __eq__(self, other):
        ''' (Horario, Horario) -> boolean
        Recebe dois parametros, self e other, e compara os dois
        para saber se são iguais.
        '''
        self_seg = transf_horario_segundos(self)
        other_seg = transf_horario_segundos(other)

        if self_seg == other_seg:
            return True
        else:
            return False

    def __ne__(self, other):
        ''' (Horario, Horario) -> boolean
        Recebe dois parametros, self e other, e compara os dois
        para saber se são diferentes.
        '''
        self_seg = transf_horario_segundos(self)
        other_seg = transf_horario_segundos(other)

        if self_seg != other_seg:
            return True
        else:
            return False

    def __ge__(self, other):
        ''' (Horario, Horario) -> boolean
        Recebe dois parametros, self e other, e compara os dois
        para saber se self é maior ou igual ao other.
        '''

        self_seg = transf_horario_segundos(self)
        other_seg = transf_horario_segundos(other)

        if self_seg >= other_seg:
            return True
        else:
            return False

    def __gt__(self, other):
        ''' (Horario, Horario) -> boolean
        Recebe dois parametros, self e other, e compara os dois
        para saber qual é o maior.
        '''
        self_seg = transf_horario_segundos(self)
        other_seg = transf_horario_segundos(other)

        if self_seg > other_seg:
            return True
        else:
            return False

    def __le__(self, other):
        ''' (Horario, Horario) -> boolean
        Recebe dois parametros, self e other, e compara os dois
        para saber se self é menor ou igual ao other.
        '''
        self_seg = transf_horario_segundos(self)
        other_seg = transf_horario_segundos(other)

        if self_seg <= other_seg:
            return True
        else:
            return False

    def __lt__(self, other):
        ''' (Horario, Horario) -> boolean
        Recebe dois parametros, self e other, e compara os dois
        para saber qual é o menor.
        '''
        self_seg = transf_horario_segundos(self)
        other_seg = transf_horario_segundos(other)

        if self_seg < other_seg:
            return True
        else:
            return False

    # ------------------------------------------------------------------------------
    # INSIRA OUTROS MÉTODOS DA CLASSE HORARIO AQUI
    # ------------------------------------------------------------------------------

    # ------------------------------------------------------------------------------
    #     FIM DA CLASSE HORARIO
    # ------------------------------------------------------------------------------


# ===================================================================
#  Insira as funções que desejar aqui. CUIDADO com a tabulação.
# ===================================================================

def h_min(seq):
    '''(list) -> Horario
    Recebe uma lista seq com um ou mais objetos do tipo Horario.
    Retorna uma referência para um objeto Horario de menor valor em seq.
    '''
    h_menor = seq[0]

    for i in range(1, len(seq)):
        if seq[i] < h_menor:
            h_menor = seq[i]

    return h_menor


def transf_horario_segundos(horario):
    ''' (Horario) -> int
    Recebe um Horario e o transforma em segundos
    '''

    horas_seg = horario.dados[2] * 3600  # Transforma horas em segundos
    minutos_seg = horario.dados[1] * 60  # Transforma minutos em segundos
    seg = horario.dados[0]

    total_seg = int(horas_seg + minutos_seg + seg)  # Soma o total de segundos

    return total_seg


def transf_segundos_horario(segundos):
    ''' (int) -> (Horario)
    Recebe um int que representa a quantidade de segundos e transforma em um tipo Horario
    '''
    horas = segundos // 3600  # Transforma os segundos em hora
    segundos = segundos % 3600
    minutos = segundos // 60  # Transforma os segundos restantes em minutos
    segundos = segundos % 60  # Guarda os segundos que sobraram

    return Horario(horas, minutos, segundos)


####### ========================================================== #######
#####
##     NAO REMOVA OU MODIFIQUE AS LINHAS A SEGUIR QUE TERMINAM O ARQUIVO
#####
####### ========================================================== #######
#  fim da definição de todas as funções e classes
#  chama a main
## =============================================================

if __name__ == '__main__':
    main()

