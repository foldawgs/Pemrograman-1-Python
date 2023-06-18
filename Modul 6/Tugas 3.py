def cari_penjumlahan(bilangan1,bilangan2):
    penjumlahan = bilangan1 + bilangan2
    print(f"Hasil : {penjumlahan}")

def cari_perkalian(bilangan1,bilangan2):
    perkalian = bilangan1 * bilangan2
    print(f"Hasil : {perkalian}")

def cari_pembagian(bilangan1,bilangan2):
    pembagian = bilangan1 / bilangan2
    print(f"Hasil : {pembagian}")

def cari_pengurangan(bilangan1,bilangan2):
    pengurangan = bilangan1 - bilangan2
    print(f"Hasil : {pengurangan}")

def cari_pangkat(bilangan1,bilangan2):
    pangkat = bilangan1 ** bilangan2
    print(f"Hasil : {pangkat}")

while True:
    print("\n================================")
    print("     KALKULATOR     ")
    print("1. Penjumlahan")
    print("2. Perkalian")
    print("3. Pembagian")
    print("4. Pengurangan")
    print("5. Pangkat")

    pilihan = int(input("Masukan Pilihan: "))
    if pilihan == 1:
        bilangan1 = int(input("Masukan bilangan 1: "))
        bilangan2 = int(input("Masukan bilangan 2: "))
        cari_penjumlahan(bilangan1,bilangan2)
    elif pilihan == 2:
        bilangan1 = int(input("Masukan bilangan 1: "))
        bilangan2 = int(input("Masukan bilangan 2: "))
        cari_perkalian(bilangan1,bilangan2)
    elif pilihan == 3:
        bilangan1 = int(input("Masukan bilangan 1: "))
        bilangan2 = int(input("Masukan bilangan 2: "))
        cari_pembagian(bilangan1,bilangan2)
    elif pilihan == 4:
        bilangan1 = int(input("Masukan bilangan 1: "))
        bilangan2 = int(input("Masukan bilangan 2: "))
        cari_pengurangan(bilangan1,bilangan2)
    elif pilihan == 5:
        bilangan1 = int(input("Masukan bilangan 1: "))
        bilangan2 = int(input("Masukan bilangan 2: "))
        cari_pangkat(bilangan1,bilangan2)
    else:
        print("Masukan pilihan antara 1-6!")

    konfirmasi = input("Apakah anda ingin keluar dari program? (Y/N): ")
    if konfirmasi.lower() == "y" or konfirmasi.lower() == "yes":
        print("Keluar dari program")
        break