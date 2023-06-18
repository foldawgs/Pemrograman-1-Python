
jumlah_kata = int(input("Masukan jumlah kata: "))
array = []

for i in range(jumlah_kata):
    kata = input(f"Masukan kata ke {i + 1}: ")
    array.append(kata)

inputan = input(f"Masukan kata yang dicari: ")

if inputan in array:
    indeks = array.index(inputan)
    print(f"Kata ditemukan di kata ke-{indeks + 1}")
else:
    print("Kata tidak ditemukan")