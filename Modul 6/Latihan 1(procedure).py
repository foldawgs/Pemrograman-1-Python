#menggunakan procedure
def keliling_luas_persegi(sisi):
    keliling = 4 * sisi
    luas = sisi * sisi
    print("Keliling persegi: %d" % keliling)
    print("Luas persegi: %d" % luas)

panjang = int(input("Masukan panjang sisi: "))
keliling_luas_persegi(panjang)
