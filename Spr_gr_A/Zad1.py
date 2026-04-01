plik = open('prostokaty.txt')
dane = plik.readlines()

prostokaty = []

for w in dane:
    #print(w)
    para = w.split()
    #print(para)
    prostokat = (int(para[0]), int(para[1]))
    #print(prostokat)
    prostokaty.append(prostokat)
print(prostokaty)

#zadanie 1.1.
prostokaty.sort(key = lambda x: x[0] * x[1])
print(prostokaty[0], prostokaty[-1])
p_min = prostokaty[0]
p_max = prostokaty[-1]

print(p_min[0] * p_max[1], p_max[0] * p_max[1])

#Zadanie 1.2.
obwody = []

for p in prostokaty:
    obwod = 2 * p[0] + 2 * p[1]
    obwody.append(obwod)
print(len(set(obwody)))