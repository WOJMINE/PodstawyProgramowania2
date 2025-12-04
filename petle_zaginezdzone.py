
for w in range(1, 11):
    for o in range(1, 11):
        print(w * o, end = '\t')
    print()

#Trójkąt prostokątny
#Sposób 1
n = int(input('Wysokość trójkąta = '))
for x in range(n):
    for y in range(x + 1):
        print('*', end = '')
    print()
#Sposób 2 (Łatwiejszy)
d = int (input('Wysokość trójkąta = '))
for r in range(d):
    print('*' * (d + 1))

#Trójkąt równoramienny dowolny
f = int(input('Wysokość trujkąta = '))
spacje = n - 1
gwiazdki = 1

for z in range(n):
    print(' ' * spacje, end = '')
    print('*' * gwiazdki)
    spacje = spacje - 1
    gwiazdki = gwiazdki + 2

dbc = chr(2137)
print(dbc)