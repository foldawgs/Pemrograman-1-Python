print("=====Mengidentifikasi Tahun Kabisat=====")
year = int(input("Masukan Tahun: "))

if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"Tahun {year} adalah tahun kabisat")
else:
    print(f"Tahun {year} adalah bukan tahun kabisat")