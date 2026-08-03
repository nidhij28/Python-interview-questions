mylist1 = ["apple", "banana", "apple", "cherry", "watermelon"]
mylist2 = ["apple", "raspberry", "cherry", "blueberry", "guava"]

set1 = set(mylist1)
set2 = set(mylist2)

set3 = set1.difference(set2)
newlist = list(set3)

print(newlist)