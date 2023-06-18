
operasi_katarak = "Rp.7.500.000"
operasi_plus_minus = "Rp.5.000.000"
operasi_silinder = "Rp.4.000.000"
operasi_jantung_koroner = "Rp.500.000.000"
operasi_katup_jantung = "Rp.350.000.000"
operasi_otot_jantung = "Rp.450.000.000"

print("--- Menu Hitung Biaya Operasi ---")
print(f"1. Hitung Biaya Operasi Mata\n2. Hitung Biaya Operasi Jantung")

inputan = int(input("Masukan pilihan: "))
if inputan == 1:
    print("\nOperasi Mata")
    print("1. Katarak\n2. Plus/Minus\n3. Silinder")
    inputan = int(input("Masukan Pilihan:  "))
    if inputan == 1:
        print(f"Biaya operasi mata katarak adalah = {operasi_katarak}")
    elif inputan == 2:
        print(f"Biaya operasi mata plus/minus adalah = {operasi_plus_minus}")
    elif inputan == 3:
        print(f"Biaya operasi mata silinder adalah = {operasi_silinder}")
    else:
        print("Harap pilih sesuai angka yang tertera (1/2/3)")
elif inputan == 2:
    print("\nOperasi Jantung")
    print("1. Jantung Koroner\n2. Katup Jantung\n3. Otot Jantung")
    inputan = int(input("Masukan Pilihan:  "))
    if inputan == 1:
        print(f"Biaya operasi jantung koroner adalah = {operasi_jantung_koroner}")
    elif inputan == 2:
        print(f"Biaya operasi katup jantung adalah = {operasi_katup_jantung}")
    elif inputan == 3:
        print(f"Biaya operasi otot jantung adalah = {operasi_otot_jantung}")
    else:
        print("Harap pilih sesuai angka yang tertera (1/2/3)")
else:
    print("Harap pilih sesuai angka yang tertera (1/2)")