#Zadanie 2.
'''lista = [178, 192, 184, 182, 180, 179, 186, 190, 191, 191]

x_max = max(lista)
x_min = min(lista)

lista_norm = [(x - x_min) / (x_max - x_min) for x in lista]
print(lista_norm)'''
#Zadanie 3.
lista = [123, 89, 5600, 432, 11, 45, 900, 123450, 1410, 390, 9999]
#lista = [x for x in lista if x < 1000 or x > 9999]
lista = [x for x in lista if not(x >= 1000 and x <= 9999)]