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

#Dom. 2.4; 2.5; 2.6; 2.7; 2.8