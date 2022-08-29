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

    print("\nChamadas dentro de print")
    print(f"c0 = {c0}")  # chama __str__
    print(f"c1 = {c1}")
    print(f"c2 = {c2}")

    print("\nResultados dos métodos")
    print(f'C3 = {c0 + c1}')
    print(f'C4 = {c1 * c2}')
    print(f'C4 = {c1 - c2}')


class Complexo:
    def __init__(self, r=0.0, i=0.0):
        ''' (Complexo, float, float) -> None
        '''
        num = complex(r, i)
        self.real = num.real
        self.imag = num.imag


    def __str__(self):
        '''(Complexo) -> str
        '''
        if self.imag < 0:
            return f'{self.real} - {-self.imag}i'
        return f'{self.real} + {self.imag}i'


    def __add__(self, other):
        '''(Complexo, Complexo) -> Complexo
        Recebe uma referência `self` e outra referência `other`,
        para dois objetos da classe Fraction. Retorna uma nova fração com o
        resultado da multiplicação self * other
        '''

        real = self.real + other.real
        imag = self.imag + other.imag

        return Complexo(real, imag)


    def __sub__(self, other):
        '''(Complexo, Complexo) -> Complexo
        Recebe uma referência `self` e outra referência `other`,
        para dois objetos da classe Fraction. Retorna uma nova fração com o
        resultado da multiplicação self - other
        '''

        real = self.real - other.real
        imag = self.imag - other.imag

        return Complexo(real, imag)


    def __mul__(self, other):
        '''(Complexo, Complexo) -> Complexo
        Recebe uma referência `self` e outra referência `other`,
        para dois objetos da classe Fraction. Retorna uma nova fração com o
        resultado da multiplicação self * other
        '''

        real = (self.real * other.real) + (self.imag * other.imag)
        imag = (self.real * other.imag) + (self.imag * other.real)

        return Complexo(real, imag)


if __name__ == '__main__':
    main()