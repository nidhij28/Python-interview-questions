def check_element(arr, x):
    for num in arr:
        if num == x:
            return "present"

    return "absent"


arr = [1,2,3,4,5]
print(check_element(arr, 6))
print(check_element(arr, 3))
