dibagi = int(input("Masukan angka yang mau dibagi :"))
pembagi = int(input("Masukan angka pembagi :"))

if pembagi == 0:
    print("Pembagi tidak boleh 0")
else:
    itung = dibagi / pembagi
    print(f"Hasilnya adalah: {itung}")