def main():
    ''' Testes da classe Complexo
    '''

    print("Testes da classe Complexo\n")

    c0 = Complexo() # construtor chama __init__()
    print(f"Atributos: real = {c0.real} e imag = {c0.imag}")

    c1 = Complexo(9)
    print(f"Atributos: real = {c1.real} e imag = {c1.imag}")

    c2 = Complexo(7, 5)
    print(f"Atributos: real = {c2.real} e imag = {c2.imag}")

    c3 = Complexo(-1, 3)
    print(f"Atributos: real = {c3.real} e imag = {c3.imag}")

    c4 = Complexo(2, -8)
    print(f"Atributos: real = {c4.real} e imag = {c4.imag}")

    c5 = Complexo(-3, -4)
    print(f"Atributos: real = {c5.real} e imag = {c5.imag}")

    i1 = 10

    print("\nChamadas dentro de print")
    print(f"c0 = {c0}")  # chama __str__
    print(f"c1 = {c1}")
    print(f"c2 = {c2}")
    print(f'c3 = {c3}')
    print(f'c4 = {c4}')
    print(f'c5 = {c5}')

    print("\nResultados dos métodos")
    print(f'({c0}) + ({c1}) = {c0 + c1}')
    print(f'({c1}) * ({c2}) = {c1 * c2}')
    print(f'({c1}) - ({c2}) = {c1 - c2}')
    print(f'{i1} * ({c2}) = {i1 * c2}')
    print(f'({c2}) / {i1} = {c2 / i1}')
    print(f'{i1} / ({c2}) = {i1 / c2}')


class Complexo:
    def __init__(self, r=0.0, i=0.0):
        ''' (Complexo, float, float) -> None
        '''
        self.real = float(r)
        self.imag = float(i)


    def __str__(self):
        '''(Complexo) -> str
        '''
        if self.imag >= 0:
            return f'{self.real}+j{self.imag}'
        return f'{self.real}-j{abs(self.imag)}'

    def __add__(self, other):
        '''(Complexo, Complexo) -> Complexo
        Recebe uma referência `self` e outra referência `other`,
        para dois objetos da classe Fraction. Retorna uma nova fração com o
        resultado da adição self + other
        '''

        if type(other) is int or type(other) is float:
            real = self.real + other
            imag = self.imag
        else:
            real = self.real + other.real
            imag = self.imag + other.imag

        return Complexo(real, imag)

    def __radd__(self, other):
        ''' (Complexo, int/float) -> Complexo / int/float
        Recebe dois tipos numéricos, sendo um deles um Complexo, e inverte suas posições na operação
        para que seja possível realizar seu cálculo
        '''
        return self + other

    def __sub__(self, other):
        '''(Complexo, Complexo) -> Complexo
        Recebe uma referência `self` e outra referência `other`,
        para dois objetos da classe Fraction. Retorna uma nova fração com o
        resultado da subtração self - other
        '''

        if type(other) is int or type(other) is float:
            real = self.real - other
            imag = self.imag
        else:
            real = self.real - other.real
            imag = self.imag - other.imag

        return Complexo(real, imag)

    def __rsub__(self, other):
        ''' (Complexo, int/float) -> Complexo / int/float
        Recebe dois tipos numéricos, sendo um deles um Complexo, e inverte suas posições na operação
        para que seja possível realizar seu cálculo
        '''
        return self - other

    def __mul__(self, other):
        '''(Complexo, Complexo) -> Complexo
        Recebe uma referência `self` e outra referência `other`,
        para dois objetos da classe Fraction. Retorna uma nova fração com o
        resultado da multiplicação self * other
        '''

        if type(other) is int or type(other) is float:
            real = self.real * other
            imag = self.imag * other
        else:
            real = (self.real * other.real) - (self.imag * other.imag)
            imag = (self.real * other.imag) + (self.imag * other.real)

        return Complexo(real, imag)

    def __rmul__(self, other):
        ''' (Complexo, int/float) -> Complexo / int/float
        Recebe dois tipos numéricos, sendo um deles um Complexo, e inverte suas posições na operação
        para que seja possível realizar seu cálculo
        '''
        return self * other

    def __truediv__(self, other):
        '''(Complexo, Complexo) -> Complexo
        Recebe uma referência `self` e outra referência `other`,
        para dois objetos da classe Fraction. Retorna uma nova fração com o
        resultado da divisão self / other
        '''

        if type(other) is int or type(other) is float:
            real = self.real / other
            imag = self.imag / other
        else:
            real = (self.real * other.real) + (self.imag * other.imag) / (other.real**2 + other.imag**2)
            imag = (self.imag * other.real) - (self.real * other.imag) / (other.real**2 + other.imag**2)

        return Complexo(real, imag)

    def __rtruediv__(self, other):
        ''' (Complexo, int/float) -> Complexo / int/float
        Recebe dois tipos numéricos, sendo um deles um Complexo, e inverte suas posições na operação
        para que seja possível realizar seu cálculo
        '''
        real = (other * self.real) / (self.real**2 + self.imag**2)
        imag = (other * (-self.imag)) / (self.real**2 + self.imag**2)
        return Complexo(real, imag)


if __name__ == '__main__':
    main()