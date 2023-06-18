#menggunakan selection sort
def urutNama(arr):
    n = len(arr)
    
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr

nama = ['Zhafira', 'Nirmala', 'Aksara', 'Nalendra', 'Cakra', 'Sastra', 'Agni', 'Bagas', 'Jerome', 'Kiara']
print(f"Nama sebelum diurutkan: {nama}")
urutNama(nama)
print(f"Nama sesudah diurutkan: {nama}")

