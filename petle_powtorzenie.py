lista = [10, 56, 89, 59]

#1. Chodzenie bespośrednio po elementach listy
# Do zmiennej b trafiają bespośrednio elementy listy, tzn.10, 56, 89, 59
for b in lista:
    print(b)

#2. Chodzenie po liście z użyciem indeksów
#2.1. Co to jest indeks?
# lista[2]
# 2 - indeks
#lista[2] - element znajdujący pod indeksem 2 = 89

#2.2.
for k in range(0, 4): #range(0, 4)
    print(lista[k])
