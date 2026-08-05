mylist = [1,2,2,3,3,3,4,5,6]

unique_list = []

[unique_list.append(x) for x in mylist if x not in unique_list]

print(unique_list)