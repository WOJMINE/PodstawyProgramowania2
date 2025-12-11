#Zadanie 1.
n = int(input('Podaj liczbę: '))

iloczyn = 1

for x in range(n):
    iloczyn = iloczyn * (x + 1)

    print(iloczyn)
#Zadanie 2.
lista = [4, 12, 8, 1, 5, 6, 3]
numerki = 0
for e in range(len(lista)):
    for f in range(len(lista)):
        if e != f and e in lista and f in lista and (e + f) % 3 == 0:
           numerki += 1
print(numerki)

#Zadanie 3.
g = int(input('Podaj ile będzie napisów'))
max_napis = ''
for x in range(n):
    napis = input('Podaj napis')
    ile_a = napis.count('a')
    max_ile_a = max_napis.count('a')
    if ile_a > max_ile_a:
        max_napis = napis
print(max_napis)