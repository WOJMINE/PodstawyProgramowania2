#Zadanie 15.
#a)
X = list(range(0, 103, 3))
print(f'x\ty')

for x in X:
    y = 0.5 * x + 3
    #print(x, y)
    print(f'{x}\t{y}')
#Tak tez można
print(f'x\ty')

for x in range(0, 103, 3):
    y = 0.5 * x + 3
    #print(x, y)
    print(f'{x}\t{y}')

#b)
print(f'x\ty')
for x in range(-30, 61):
    x = x / 10
    y = 0.5 * x + 3
    #print(x, y)
    if x >= 0:
        print(f'{x}\t{y}')
    else:
        print(f'{x}\t{y}')

#Zadanie 16,
lista1 = list(range(3, 31, 3))
lista2 = list(range(11, 111, 11))
lista3 = list(range(13, 131, 13))

#Sposób 1.
for x, y, z in zip(lista1, lista2, lista3):
    print(f'{x}\t{y}\t{z}')

#Sposób 2.
for i in range(10):
    print(f'{lista1[i]}\t{lista2[i]}\t{lista3[i]}')

lista10 = [10, 56, 89, 59]

for q in lista10:
    print(q)
for i in range(len(lista10)):
    print(lista1)

#Zadnie 17.
n = int(input('Podaj ile będzie liczb'))
suma = 0

for x in range(n):
    liczba = int(input('Podaj ile będzie liczb'))
    suma = suma + liczba

print(suma)