'''plik = open('dane.txt')
dane = plik.read()
print(dane)'''
from email.iterators import typed_subpart_iterator

'''plik2 = open('dane2.txt')
dane2 = plik2.readlines()

for i in range(len(dane2)):
   dane2[i] = int(dane2[i])
print(dane2)'''

'''plik3 = open('dane_tszy.txt')
dane3 = plik3.readlines()

for i in range(len(dane3)):
 dane3[i] = dane3[i].strip()'''

'''plik4 = open( ' dane4.txt')
dane4 = plik4.readlines()

for i in range(len(dane4)):
 dane4[i] = dane4[i].split()
print(dane4)'''

plik5 = open( 'dane5.txt' )
dane5 = plik5.readlines()

for i in range(len(dane5)):
 dane5[i] = dane5[i].split()
 for j in range(len(dane5[i])):
  dane5[i][j] = int(dane5[i][j])
print(dane5)

dane5_prim = [list(map(int, w.split())) for w in open('dane5.txt')]
print(dane5_prim)
