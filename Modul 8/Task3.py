def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

arr = [17, 2, 15, 7, 72, 31, 12, 57, 63, 71, 23, 92, 1]

print("Daftar sebelum diurutkan:", arr)
bubble_sort(arr)
print("Daftar setelah diurutkan:", arr)
target = int(input("Masukan angka yang ingin dicari: "))

index = binary_search(arr, target)
if index != -1:
    print(f"Angka {target} ditemukan pada indeks ke {index}.")
else:
    print(f"Angka {target} tidak ditemukan dalam daftar.")
