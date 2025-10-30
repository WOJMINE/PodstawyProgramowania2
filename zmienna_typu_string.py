napis = 'informatyka'

#I. Fragment tekstu:
#1) wycinanie od ... do
print(napis[2:5]) #czylt tak naprawdę od 2 do 4

#2) wycinanie od ... do co ileś
print(napis[2:10:2])

#3) wycinanie od początku
print(napis[:3])

#4) wycinanie od końca
print(napis[7:])

#5) czytanie od końca
print(napis[::-2])

#II. Zawieranie się znaku w słowie
if 'a' in napis:
    print('należy')
else:
    print('nie należy')

#III.łączenie napisów (konkatenacja)
napis2 = napis +'jestnajlepsza'
print(napis2)

#IV. Funkcje zmiennych typu string

#1) poszukiwanie danego fragmentu w tekście
napis3 = 'matematyka'
index_gdzie_jest = napis3.find('tem')
print(index_gdzie_jest)

napis4 = 'alabalalalabala'
index_gdzie_jest2 = napis4.find('bala')
index_gdzie_jest3 = napis4.find('bala', index_gdzie_jest2 + 1)
index_gdzie_jest4 = napis4.find('xyz',index_gdzie_jest2 + 1)
print(index_gdzie_jest2)
print(index_gdzie_jest3)
print(index_gdzie_jest4)

if napis4.find('xyz') != -1:
    print('xyz jest w napisie')
else:
    print('xyz nie jest w napisie')

#2.)Podział tekstu na fragmenty
'''piec_liczb = input('Podaj pięć liczb. Oddziel je przecinkiem: ')
piec_liczb_po_podziale = piec_liczb.split(',')
print(piec_liczb_po_podziale)
trzecia_liczba = int(piec_liczb_po_podziale[2])
print(trzecia_liczba + 33)
'''

#3.) Łączenie naoisów
lista_napisów = ['Windows', 'jest', 'tworzony', 'dla', 'kasy']
cale_zdanie = '$'.join(lista_napisów)
print(cale_zdanie)

lista_napisów2 = ['abc', 'xyz', 'bbc', 'tvn']
cale_zdanie2 = '\n',join(lista_napisów2)
print(cale_zdanie2)

#4.) Zliczanie daniego znaku w tekście
napis5 = 'prawdopodobieństwo'
ile_razy_o = napis5.count('o')
print(ile_razy_o)