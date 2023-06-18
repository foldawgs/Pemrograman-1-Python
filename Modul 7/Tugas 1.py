#menggunakan bubble sort
def urutNilai(array):
    n = len(array)

    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array
    
arrayNilai = [3.8, 2.9, 3.3, 4.0, 2.7]

print("\nIndeks Prestasi Semester (IPS)")
print(f"List sebelum diurutkan : {arrayNilai}")
hasil = urutNilai(arrayNilai)
print(f"List sesudah diurutkan : {arrayNilai}")
