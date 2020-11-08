# coding: utf-8
from numpy import arccos,sqrt, pi

def trojkaty(a, b, c):
    " sprwadzanie czy dane są większe od zera"
    if min(a, b, c) > 0:
        if sum([a, b, c]) - max(a, b, c) > max(a, b, c):
            p = (sum([a, b, c]) / 2)
            P = (p * (p - a) * (p - b) * (p - c)) ** 0.5
            alfa = arccos((b**2+c**2-a**2)/(2*b*c)) # todo: zamienieć na cosinusy alfa = acos((a^2+b^2-c^2)/(2*a*b))
            beta = arccos((a**2+c**2-b**2)/(2*a*c))
            gamma = arccos((a**2+b**2-c**2)/(2*a*b))
            if max(alfa,beta,gamma) < pi/2:
                kat = ('ostrokątnego')
            elif max(alfa,beta,gamma) == pi/2:
                kat = ('prostokątnnego')
            else:   # todo: rozwarto konntny nie wyświtala sie
                kat = ('rozwartokątnego')

            print('Pole powierzchni trójkąta '+ kat + f' {a} , {b} i {c} wynosi {P:.4f}')  # .4f to dokładność wyświetlania wyniku
            return (P)
        else:  # suma długości mniejszych boków nie jest większa od długości najdłuższego
            print(f'Podane liczby {a}, {b} i {c} nie są długościami boków trójkąta')
    else:  # conajmniej jeden z boków jest równy lub mniejszy od zera
        print("Błędne dane, długości boków niemogą być równe lub mniejsze od zera")

trojkaty(3,4,5)
trojkaty(4,4,5)
trojkaty(3,4,6)