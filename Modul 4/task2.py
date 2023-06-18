
bilangan = int(input(f"Masukan Bilangan : "))
pangkat = int(input(f"Masukan Pangkat : "))
hasil = 1
for i in range(pangkat):
    hasil *= bilangan
print(hasil)
