zbior = set() #Pusty zbiór

lista2d = [
[5, 2, 8, 5, 1],
[3, 8, 2, 9, 5],
[1, 4, 4, 2, 7],
[6, 3, 9, 1, 4],
[8, 2, 5, 6, 3]
]

for x in range(len(lista2d)):
    for y in range(len(lista2d[0])):
        element = lista2d[x][y]
        zbior.add(element)

print(zbior)

zbior_caly = set()
for x in lista2d:
    zbior2 = set(x)
    zbior_caly = zbior_caly.union(zbior2)

print(zbior_caly)

#Zadanie 1.2.
lista1d = []
for x in range(len(lista2d)):
    for y in range(len(lista2d[0])):
        element = lista2d[x][y]
        lista1d.append(element)

lista1d_zbior = set(lista1d)
for e in lista1d_zbior:
    print(e, lista1d.count(e))

slowa = [
"LETTER",
"BALLOON",
"SUCCESS",
"HAPPY",
"COFFEE",
"BOOKKEEPER",
"ASSESS",
"MISSISSIPPI",
"ADDRESS",
"TOOLBOX"
]
slowo = 'LETTER'
slowo_zbior = set(slowo)
print(slowo_zbior)

#Sposób 1
max_x = ''
max_l_r_l = 0
for x in slowa:
    x_zbior = set(x)
    l_r_l = len(x_zbior)
    if l_r_l > max_l_r_l:
        max_l_r_l = l_r_l
        max_x = x
    print(max_x)

#Sposób 2
max_slowo = max(slowa, key = lambda x: len(set(x))) #nie trzeba
print(max_slowo)

#print(f'{x} {len(x_zbior)}')

#Zadanie 2.2.
zbior = set()
for x in slowa:
    for y in x:
        zbior.add(y)
print(zbior)

for l in zbior:
    lista = []
    for s in slowa:
        if l in s:
            lista.append(s)
        print(f'{l}: {lista}')