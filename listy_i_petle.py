#1. powtarzanie wielokrotnie powtarzanych czynności

#1.1. Jak nie programować wielokrotnie powtarzalnych czynności

'''a = float(input('Podaj liczbę'))
b = float(input('Podaj liczbę'))
c = float(input('Podaj liczbę'))
d = float(input('Podaj liczbę'))
e = float(input('Podaj liczbę'))

suma = (a + b + c + d)

print(suma)'''

#1.2. Ta forma jest poprawna

liczba = 0
suma = 0

for i in range(5):
    liczba = float(input('Podaj liczbę'))
    suma = suma + liczba

    print(suma)

#2. Listy

lista = ['qwerty', 56, [6, 7], 4.56, [[5, 8], 1]]
print(lista[2][1])
print(lista[4][0][1])

#2. Listy i pętle

lista2 = ['kot','pies', 'owca', 'lama']
#Pętla for:
#-> wycięcia dane z listy (jedna po drugiej)
#-> wykonuje się tyle razy ile elementów ma lista
for z in lista2:
    print(z)

#Pętla, która wykona się 3 razy
lista3 = [1410, 15, 7]

for i in lista3:
    print('OK')

#Pętla, która wykonuje się1000 razy
lista4 = [0] * 1000
print(lista4)

#Pętla, która wykouje się 1000 razy

lista4 = [[0] * 1000 for i in range(10)]
print(lista4)
for i in lista4:
    print('Cześć')

#4. Generatory i pętle
przedzial = range(1,10) #{1, 2, 3, 4, 5, 6, 7, 8, 9}

for i in przedzial:
    print(i)

#Pętla, ktora wykona się 10 razy
for i in range(10): #range(0, 10), 10 - liczba powtórzeń
    print(i)

'''lista5 = [0]

for i in lista:
    print('Cześć')
    lista.append(8)'''

#4. Pętla while
liczba = 5

while liczba > 0:
    print(liczba)
    liczba = liczba - 1