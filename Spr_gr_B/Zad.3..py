plik = open('ruch.txt')
dane = plik.readlines()
print(dane)

for i in range(len(dane)):
    dane[i] = dane[i].split()
    #dane[i] = [float(dane[i][0], float(dane[i][1]))]
    dane[i] = list(map(float, dane[i]))

print(dane)

def t(i):
    return (i - 1) / 100

def v_sr(rk, rp, dt):
    return [(rk[0] - rp[0]) / dt, (rk[1] -rp[1])]

def szyb_sr(v_sr):
    return (v_sr[0] ** 2 + v_sr[1] ** 2) ** 0.5
wynik = []
for x in range(1, len(dane)):
    rp = dane[0]
    rk = dane[i]
    czas = t(i + 1)
    pr_sr = v_sr(rk, rp, czas)
    szybkosc_sr = szyb_sr(pr_sr)
    wynik.append((czas, szybkosc_sr))

print(wynik)