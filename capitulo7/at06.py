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

    hora = transf_horario_segundos(Horario(23, 59, 59))
    print(hora)

    hora = transf_segundos_horario(3600)
    print(hora)

    '''
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
    '''


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

        if type(other) is int:
            seg = self.dados[0]
            minutos = self.dados[1]
            hora = self.dados[2] + other
        elif type(other) is float:
            # other = transf(other)
            seg = self.dados[0] + other.dados[0]
            minutos = self.dados[1] + other.dados[1]
            hora = self.dados[2] + other.dados[2]
        else:
            seg = self.dados[0] + other.dados[0]
            minutos = self.dados[1] + other.dados[1]
            hora = self.dados[2] + other.dados[2]

        if seg > 59:
            minutos += seg // 60
            seg = seg % 60
        if minutos > 59:
            hora += minutos // 60
            minutos = minutos % 60

        return Horario(hora, minutos, seg)

    def __radd__(self, other):
        ''' (Horario, Horario) -> (Horario) + (Horario)
        '''
        return self + other

    def __sub__(self, other):
        ''' (Horario, Horario) -> (Horario)
        Recebe dois parâmetros, self e other, e soma os dois Horarios.
        '''

        if type(other) is int:
            seg = self.dados[0]
            minutos = self.dados[1]
            hora = self.dados[2] - other
        elif type(other) is float:
            # other = transf(other)
            seg = self.dados[0] - other.dados[0]
            minutos = self.dados[1] - other.dados[1]
            hora = self.dados[2] - other.dados[2]
        else:
            seg = self.dados[0] - other.dados[0]
            minutos = self.dados[1] - other.dados[1]
            hora = self.dados[2] - other.dados[2]

        if seg > 59:
            minutos += seg // 60
            seg = seg % 60
        if minutos > 59:
            hora += minutos // 60
            minutos = minutos % 60

        return Horario(hora, minutos, seg)

    def __rsub__(self, other):
        ''' (Horario, Horario) -> (Horario) - (Horario)
        '''
        # other = transf(other)
        return self - other

    def __lt__(self, other):
        self_seg = transf_horario_segundos(self)
        other_seg = transf_horario_segundos(other)
        if self.dados[2] < other.dados[2]:
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

    total_seg = horas_seg + minutos_seg + seg  # Soma o total de segundos

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

