
def urutBuku(array):
    banyak_buku = len(array)

    for i in range(1, banyak_buku):
        key = array[i]
        j = i - 1

        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key

    return array

judul = []

banyak_buku = int(input("Masukkan Jumlah Judul Buku: "))
for i in range(banyak_buku):
    inputan = input("Masukkan Judul Buku ke-{}: ".format(i+1))
    judul.append(inputan)

print("\n===== Cara Pengurutan =====")
print("1. Insertion Ascending")
print("2. Insertion Descending")
pilihan = int(input("Pilih: "))
if pilihan == 1:
    hasil_sort = urutBuku(judul)
else:
    hasil_sort = urutBuku(judul)[::-1]

print("\nHasil setelah di sorting:")
for inputan in hasil_sort:
    print(inputan)