#1) Listy a napisy
napis = 'informatyka'

lista = []
for l in napis:
    lista.append(l)
print(lista)

#2) Zamiana napisu na listę
lista2 = list(napis)
print(lista2)

#Zakres i lista
zakres = range(3, 10, 2)
lista3 = list(zakres)
print(lista3)

#3 Indeksowanie elementów listy
lista4 = ['osa', 99, 3.14, [5, 7, 8, 9]]
print(lista4[1:3]) #wycinanie fragmentu listy
print(lista4[3][2]) #obsługa listy zagnieżdżonej
print(lista4[3][::2]) #obsługa listy zagnieżdżonej

#4) Powielanie listy
#dodawanie list
lista5 = ['a', 45, 78]
lista6 = [[4, 8], 56, 12]
lista7 = lista6 + lista5
print(lista7)

#dodawanie list 2
lista8 = ['a', 45, 78]
lista9 = [[4, 8], 56, 12]
lista8.extend(lista9)
print(lista8)

#"mnożenie" listy przez liczbę
lista10 = [0] * 1000
lista11 = [[0] * 10] * 10
lista11[0][0] = 5
print(lista10)