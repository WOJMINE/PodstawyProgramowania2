#Zadanie 1.
slowo = 'konstantynopolitanczykiewiczowianeczka'
samogloski = ['a', 'e', 'i', 'o', 'u', 'y']
slowo2 = ''.join([x for x in list(slowo) if x not in samogloski])
print(slowo2)

#Zadanie 2.
lista1 = ['kot', 'mysz', 'pies']
lista2 = [lista1, lista1 * 3, 4, 8, 9, [10, 11, 12, 13, 1], lista1 + lista1]

zagniezdzona = lista2[5][1:4]
print(zagniezdzona)

#Zadanie 3.
liczby = ['123', '56', '7890', '59', '456', '822']
lista_liczb = list(map(int, liczby))
print(sum(lista_liczb))

print(sum(list(map(int, ['123', '56', '7890', '59', '456', '822']))))

#Zadanie 4.
suma = 0
lista2d = [[4, 9, 2, 1, 7], [11, 2, 5, 6, 1], [9, 7, 23, 0], [1, 2, 3, 4, 5]]
for i in range(len(lista2d)):
    element = lista2d[i][i]
    suma += element
print(suma)

#Zadanie 5.
oceny = {1: [2, 4, 6], 2: [1, 3, 5, 7, 11], 3: [8, 9, 10, 12, 13, 14, 15, 16, 17, 18], 4: [19, 20, 21, 22, 23, 24, 25], 5: [26, 27, 28], 6: [29]}

#a)
for o in oceny:
    print(o, len(oceny[o]))

#b)
jedynki = oceny[1]
szostki = oceny[6]
del oceny[1]
del oceny[6]
oceny[2].extend(jedynki)
oceny[5].extend(szostki)
print(oceny)

#Zadanie 6.
liczba = input('Podaj l.c.d: ')
cyfry = list(liczba)

#a)
print(len(cyfry))

#b)
zbior = set(cyfry)
print(len(zbior))

#c)
for e in zbior:
    print(f'{e}: {cyfry.count(e)}')

