def max_value(arr):
    max = arr[0]
    for num in arr:
        if num> max:
            max = num
    return max

def min_value(arr):
    min = arr[0]
    for num in arr:
        if num < min:
            min - num
    return min

print(max_value([1,2,3,4,3,2]))
print(min_value([1,2,3,4,3,2]))
