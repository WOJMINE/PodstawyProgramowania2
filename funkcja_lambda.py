dodawanie = lambda x, y: x + y

'''def dodawanie2(x, y):
    return x + y
print(dodawanie(5, 6))

lista = ['abba', 'bcca', 'ghaaaaaa', 'klaaa']
lista.sort(key = lambda x: x.count('a'))
print(lista)'''

#Zaawansowane sortowanie
lista = [6, -9, 3, 0, -12, -1, 7]

#1)SOrtowanie po wartości bezwzględnej
lista.sort(key = lambda x: abs(x))
print(lista)

#2) Sortowanie po długościach napisów
lista2 = ['matematyka', 'filozofia', 'fizyka', 'informatyka']
lista2.sort(key = lambda x: len(x)) #można dac tu minusa, wtedy bedzie od końca
print(lista2)

#3) Sortowanie wielopoziomowe
ludzie = [['Janusz', 'Baca'], ['Bartłomiej', 'Kaca'], ['Janusz', 'Aca'], ['Bartłomiej', 'Gaca']]
ludzie.sort(key = lambda x: (x[0], x[1]))
print(ludzie)

#4) Sortowanie po liczbie dzielników
def ile_dziel(liczba):
    ile = 0
    for d in range(1, liczba + 1):
        if liczba % d == 0:
            ile += 1
    return ile

lista3 = [12, 7, 1024, 9, 16]
lista3.sort(key = lambda x: ile_dziel(x))
print(lista3)

#4.2) Zaawansowane użycie funkcji map

#proste mapowanie
lista4 = [1, 5, -6, 10, -7]
kwadraty4 = list(map(lambda x: x ** 2, lista4))
print(kwadraty4)

#Zaawansowane mapowanie
slownik = {'fiz': 'fizyka', 'mat': 'matematyka', 'inf': 'informatyka'}
lista5 = ['fiz', 'jest', 'tragiczny', 'ale', 'inf', 'też', 'jednak', 'nic', 'nie', 'zastąpi', 'mat']

lista6 = list(map(lambda x: slownik[x] if x in slownik else x, lista5))
print(lista6)