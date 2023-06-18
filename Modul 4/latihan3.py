bilangan1 = int(input(f"Masukkan bilangan pertama: "))
bilangan2 = int(input(f"Masukkan bilangan kedua: "))

if bilangan1 > bilangan2:
    terbesar = bilangan1
    terkecil = bilangan2
else:
    terbesar = bilangan2
    terkecil = bilangan1

faktor = 1

for i in range(1, terkecil+1):
    if terkecil % i == 0 and terbesar % i == 0:
        faktor = i

print(f"Faktor persekutuan terbesar dari {bilangan1}, {bilangan2} adalah {faktor}")
