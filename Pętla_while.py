#Pętla while - przykłady

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
poprawne_haslo = 'DuPa'
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