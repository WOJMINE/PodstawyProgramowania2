#Zadanie 2.1.
plik = open('liczby.txt')
dane = plik.readlines()

for y in range(len(dane)):
    dane[y] = dane[y].strip()

for y in dane:
    if int(y[::-1]) % 17 == 0:
        print(y[::-1])
print(len(set(dane)))
#Zadanie 2.2.

#Ile Różnych

#Ile par
lista = []
for x in dane:
    if dane.count(x) == 2:
        lista.append(x)
print(len(lista))

#Ile trójek
lista2 = []
for i in dane:
    if dane.count(i) == 3:
        lista2.append(i)
print(len(lista2))

#Razem
licznik2 = 0
licznik3 = 0

for j in set(dane):
    if dane.count(j) == 3:
        licznik2 += 1
    elif dane.count(j) == 3:
        licznik3 += 1
print(licznik2, licznik3)
