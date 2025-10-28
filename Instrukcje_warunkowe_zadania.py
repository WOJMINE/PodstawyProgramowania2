#Rozwiązywanie równania kwadratowego
'''
a = float(input('Podaj liczbę a =/= 0: '))
b = float(input('Podaj liczbę b: '))
c = float(input('Podaj liczbę c: '))

delta = b ** 2 - 4 * a * c

if delta > 0:
    x1 = (-b - delta ** 0.5) / (2 * a)
    x2 = (-b + delta ** 0.5) / (2 * a)
    print(f'x1 = {x1} v x2 = {x2}')
elif delta == 0:
    x = (-b - delta ** 0.5) / (2 * a)
    print('x1 = x2 = {}'.format(x))
else:
    print('Brak rozwiązań')
'''
#Zadanie 12.
print('Podaj swoje wyniki: ')
pisemny_j_polski = int(input('pisemny polski'))
pisemny_obcy = int(input('pisemny obcy'))
pisemny_dodatkowy = int(input('pisemny dodatkowy'))
ustny_polski = int(input('Ustny polski'))
ustny_obcy = int(input('Ustny obcy'))

#Zad 14
a = float(input('Podaj liczbę a różną od 0: '))
b = float(input('Podaj liczbę b: '))
c = float(input('Podaj liczbę c: '))

if a == 0:
    print('Współczynnik powinien być różny od 0')
elif b == c == 0:
    print('𝑥0 = 0')

elif b == 0 and c != 0:
    if -(c / a) > 0:
        x1 = (-(c / a) ** 0.5)
        x2 = -(-(c / a) ** 0.5)
        print(f'x1 = {x1} v x2 = {x2}')
    elif -(c / a) < 0:
        print('Nie ma rozwiązań')

elif c == 0 and b != 0:
    x1 = 0
    x2 = -(b / a)
    print(f'x1 = {x1} v x2 = {x2}')

elif b != 0 and c != 0: #else
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        print(f'x1 = {x1} v x2 = {x2}')
    elif delta == 0:
        x0 = (-b) / (2 * a)
    elif delta < 0:
        print('Nie ma rozwiązań')