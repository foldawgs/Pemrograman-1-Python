def cari_keliling(jari_jari):
    keliling = 2 * 3.14 * jari_jari
    return keliling

def cari_luas(jari_jari):
    luas = 3.14 * jari_jari**2
    return luas

jari_jari = float(input("Masukan jari-jari lingkaran: "))
keliling = cari_keliling(jari_jari)
luas = cari_luas(jari_jari)
print(f"Keliling lingkaran: {keliling}")
print(f"Luas lingkaran: {luas}")