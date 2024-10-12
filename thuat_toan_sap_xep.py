arr = [3,1,5,10,9]

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break
arr = [3,1,5,10,9]
bubble_sort(arr)
print('Mảng sau khi sắp xếp: ')
print(arr)

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min = i   
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

selection_sort(arr)
print('Mảng sau khi sắp xếp:')
print(arr)

