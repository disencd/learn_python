
def bubble_sort(arr):
    n = len(arr)
    swapped = True

    x = -1
    while swapped:
        swapped = False
        x += 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True

    return arr



arr = [1,3,5,23,2,56,77,4,9]
sort_list = bubble_sort(arr)
print(sort_list)

