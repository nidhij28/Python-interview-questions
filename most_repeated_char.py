mystr = "mississipi"

mydict = {}

for char in mystr:
    mydict[char] = mydict.get(char, 0) + 1
max_count = max(mydict.values())
result = [ch for ch,val in mydict.items() if val == max_count]

print(result, max_count)


#print(mydict)
# maxcount = 0
# mrc = None
# for ch, val in mydict.items():
#     if val > maxcount:
#         maxcount = val
#         mrc = ch



# print("most repeated char is ", mrc)