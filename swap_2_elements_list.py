def swap_numbers(arr, x, y):
    if x < len(arr) and y < len(arr):
        arr[x] , arr[y] = arr[y] , arr[x]

    return arr

arr = [1,2,3,4,5]
print(swap_numbers(arr, 1, 3))