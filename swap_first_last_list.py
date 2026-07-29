def swap_elements(arr):
    if len(arr) > 1:
        arr[0] , arr[-1] = arr[-1], arr[0]
    return arr

arr = [1,2,3,4]
print(swap_elements(arr))