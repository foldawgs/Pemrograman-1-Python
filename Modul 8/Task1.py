def linear_search(keyword, data):
    found = False
    for i in range(len(data)):
        if data[i].lower() == keyword.lower():
            print(f"Plat nomor {data[i].upper()} ditemukan pada indeks {i}")
            found = True
            break
    if not found:
        print(f"Plat nomor {keyword.upper()} tidak ditemukan")

plat_nomor = ["R 2477 SR", "R 1234 DJ", "R 7015 LP", "R 0201 RR", "R 3304 DA", "R 2401 SK", "R 2103 RT", "R 1708 RI", "R 1111 SR", "R 4987 LH"]
keyword = input("Masukan plat nomor yang dicari: ")
linear_search(keyword,plat_nomor)