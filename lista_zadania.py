lista1 = [12, -9, 6, 2, 8, 1, 15, -7, 0, 1, 1, 2, 2, -7, 2, 1, -7, 2]
lista2 = [['pies', 'wilk'], ['kot domowy', 'tygrys', 'lew'], 'kapibara', 'mrówka', ['rekin', 'śledź', 'pstrąg']]

#a.
print(lista2[1][2])

#b.
mrowka = list(lista2[3])
print(mrowka[2])
print(list(lista2[3]))
#odwrotnie
slowo = ''.join(mrowka)
print(type(slowo))

#c.
lista3 = lista1[2::2]
print(lista3)

#d.
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
print(lista_a.append(6))
print(lista_a)
lista2.append(lista2[1] * 3)
print(lista2)

#e.
lista1 = lista1 + [9, 6, 16, -8, 7]
print(lista1)

#f.
lista1.sort()
print(lista1)
#Można też tak:
lista1_posortowana = sorted(lista1)
print(lista1_posortowana)
print(lista1_posortowana[0], lista1_posortowana[-1])
print(min(lista1), max(lista1))

#g.
del lista1[4]
print(lista1)

#h.
del lista1[4:9]

#i.
while 2 in lista1:
    lista1.remove(2)

lista1 = [x for x in lista1 if x != 2]
print(lista1)

#j)
# lista3 = [x ** 2 for x in lista1]
lista3 = []
for x in lista1:
    lista3.append(x ** 2)
print(lista3)