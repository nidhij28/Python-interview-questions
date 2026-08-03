list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]


# myset = set(list1) & set(list2)

# if myset:
#     print("The common values are:", myset)
# else:
#     print("No common numbers")

found_list = []
for num in list1:
    if num in list2:
        found_list.append(num)

if found_list:
    print("The common values are:", found_list)
else:
    print("no common values")
