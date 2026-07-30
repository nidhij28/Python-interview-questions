arr = [1,2,3,2,4,5,6,7]


myset = set(arr)
mylist = list(myset)
mylist.sort()

first = second = 0

for num in arr:
    if num > first:
        first = num
        second = first
    elif num > second and num != 0:
        second = num

print("second largest number is", second)

#print("second largest number is", mylist[-2])