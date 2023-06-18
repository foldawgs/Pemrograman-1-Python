def bubble_sort(data):
    for i in range(len(data)):
        for j in range(len(data) - i - 1 ):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

def binary_search(keyword, data):
    left = 0
    right = len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if str(data[mid]).lower() > keyword.lower():
            right = mid - 1
        elif str(data[mid]).lower() < keyword.lower():
            left = mid + 1
        else:
            print(data)
            print(f"Keyword {keyword} has been found at index {mid}")
            return mid
    
    print(data)
    print(f"Keyword {keyword} not found")
    return -1

data = [23, 53, 43, 78, 90, 10, 32]
bubble_sort(data)

keyword = input("Input keyword: ")
binary_search(keyword,data)