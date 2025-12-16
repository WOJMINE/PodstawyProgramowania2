#Pętla while - przykłady
import time
import random

liczba = 120
licznik = 0
while liczba > 0: #Tak długo jak liczba jest dodatnia. pętla się wykonuje
    liczba = liczba // 2
    licznik = licznik + 1

print(licznik)

#Zadanie 1.
x = input("Podaj liczbę lub q aby zakończyć: ")
licznik1 = 0
while x != 'q':
    liczba = int(x)
    if liczba < 2:
        licznik1 = licznik1 + 1
    x = input('Podaj liczbę lub q aby zakończyć')
print(licznik1)

#Zadanie 2.
poprawne_haslo = 'dupa'
haslo = input('Podaj hasło')
proba = 1

while haslo != poprawne_haslo and proba <= 5:
    print('Błędne hasło, podaj jeszcze raz!')
    haslo = input('Podaj hasło')
    proba = proba + 1

if haslo == poprawne_haslo:
    print('Witaj w systemie')

else:
    print('Nie ma hasła - nie ma dostępu')

#Dom. zad. 2 i 3 z teams
#(Jest na telefonie)

#Zadanie 6.
wynik1 = 0
wynik2 = 0
akcja = 0

while not ((wynik1 >= 21 or wynik2 >= 21) and abs(wynik1 - wynik2) >= 2): #abs(x) = |x|
    akcja += 1 #akcja = akcja + 1
    print(f'Akcja {akcja}')
    #druzyna = int(input('Podaj numer wygranej drużyny'))
    druzyna = random.randint(1, 2,)
    if druzyna == 1:
        wynik1 += 1
    else:
        wynik2 += 1
    print(f'Wynik {wynik1} : {wynik2}')
    time.sleep(0.1)

if wynik1 > wynik2:
    print('Wygrała drużyna 1')
else:
    print('Wygrała drużyna 2')

#Zadanie 7.
liczba2 = int(input('Podaj liczbę'))

while liczba > 0:
    cyfra = liczba % 10
    liczba2 = liczba2 // 10
    print(cyfra, end = '')

#Zadanie 8.
liczba3 = int(input('Podaj liczbę'))
d = 2
ile_czyn = 0
ile_r_czyn = 0
while liczba > 1:
    if liczba % d == 0:
        ile_r_czyn += 1
    while liczba % d == 0:
        liczba3 = liczba3 // d
        ile_czyn += 1
    d += 1
print(ile_czyn)
print(ile_r_czyn)