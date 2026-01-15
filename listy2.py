#5) Sortowanie i odwracanie listy
lista10 = [4, -1, 0, 5, 2, 9, 3]
#lista10.sort()
lista10.reverse()
print(lista10)

#6) Wyrażenia listowe (listy składne)
lista11 = list(range(1, 11))
lista11_kwadraty = [x ** 2 for x in lista11 if x % 2 == 0]
print(lista11_kwadraty)

#7) Usuwanie elementów listy
lista12 = [4, 7, 4, 8, 2, 1]
lista12.remove(4) #Usuwa pierwsze wstąpienie podanej liczby (od lewej)
while 4 in lista12:
    lista12.remove(4)
print(lista12)

#7.2) Usuwanie elementu na bazie jego indeksu
lista13 = [5, 1, 8, 3, 9, 10]
del lista13[2] #usuwamy lelement o indeksie 2
print(lista13)