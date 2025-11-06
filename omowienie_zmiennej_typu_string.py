dane = input('Podaj 5 liczb')
lista = dane.split(';')
print(lista)

wynik = ''

if int(lista[0]) > 0:
    wynki = wynik + ', ' + lista[0]
if int(lista[1]) > 0:
    wynki = wynik + ', ' + lista[1]
if int(lista[2]) > 0:
    wynki = wynik + ', ' + lista[2]
if int(lista[3]) > 0:
    wynki = wynik + ', ' + lista[3]
if int(lista[4]) > 0:
    wynki = wynik + ', ' + lista[4]