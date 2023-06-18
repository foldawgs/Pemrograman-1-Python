def banding(angka1, angka2):
    if (angka1 > angka2):
        print(f"{angka1} lebih besar daripada {angka2}")
    elif (angka1 < angka2):
        print(f"{angka1} lebih kecil daripada {angka2}")
    else:
        print(f"angka sama")

bilangan1 = int(input("Masukan bilangan 1 : "))
bilangan2 = int(input("Masukan bilangan 2 : "))
banding(bilangan1, bilangan2)