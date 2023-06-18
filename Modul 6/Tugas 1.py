def check(number):
    if number % 2 == 0:
        print(f"Bilangan {number} adalah genap")
    else:
        print(f"Bilangan {number} adalah ganjil")

number = int(input("Masukan angka: "))
check(number)