#Zadanie 0.3.
#a)
def suma_v(u, v):
    w = []
    for i in range(len(u)):
        suma = u[i] + v[i]
        w.append(suma)
    return w

u = [2, 7, 3]
v = [-1, 0, 4]

wynik = suma_v(u, v)

print(wynik)
'''
#Zadanie 2.1.
def czy_anagramy(s1, s2):
  if sorted(s1) == sorted(s2):
         return True
    else:
        return False
  return sorted(s1) == sorted(s2)

    #print(czy_anagramy('nosek', 'keson'))
    s1 = 'nosek'
    s2 = 'kseon'
print(sorted(s1) == sorted(s2))
'''
def jaki_trojkat(a, b, c):
  if a + b + c > 2 * max([a, b, c]):
    if a ** 2 + b ** 2 + c ** 2 == 2 * max([a, b, c]):
      print('prostokątny')
    elif a ** 2 + b ** 2 + c ** 2 > 2 * max([a, b, c]):
      print('ostrokątny')
    elif a ** 2 + b ** 2 + c ** 2 < 2 * max([a, b, c]):
      print('rozwartokątny')
  else:
    print('To nie jest trójkąt')


# Zadanie 2.3.
def liczby_niezaleznie(lista):
    for e in lista:
        dzielniki = []
        for l in lista:
            if e % l == 0:
                dzielniki.append(l)
        if len(dzielniki) == 1:
            wynik.append(e)
    return wynik
print(liczby_niezaleznie([12, 7, 3, 6, 21, 74]))


#Zadanie 1
def powiel(napis, n):
    return napis * n
print(powiel('Kultura ponad wszystko\n', 10))

#Zadanie 3.1
def ile_dzielnikow(liczba):
    ileliczb = 0
    for d in range(1, liczba + 1):
        if liczba % d == 0:
            ileliczb += 1
    return ileliczb
print(ile_dzielnikow(12))

#Zadanie 3.2
def czy_pierwsza(lcd):
    if lcd < 10:
        print(True)
    else:
        print(False)
    return lcd
print(czy_pierwsza(12))

#Zadanie 4
def f1(x, y):
    return x * y
def f2(f, a, b, n):
    return f(a, b) * n
print(f2(f1, 1, 2, 3, ))

def f3(x):
    return 0.5 * x ** 2 - 3
def Zwf(f, D):
    wynik4 = []
    for x in D:
        y = f(x)
        wynik4.append(y)
    return wynik4

def Zw2(f, D):
    return [f(x) for x in D]

X = [1, 2, 3, 4, 5, 6]
Y = Zwf(f3, X)
print(Y)


#Zadanie 5
def ile_liter(tekst):
    slownik = {}
    #zbior = set(tekst)
    for x in tekst:
        ile = tekst.count(x)
        slownik[x] = ile
    return slownik
print(ile_liter('babcia'))
