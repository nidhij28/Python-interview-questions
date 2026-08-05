mystring = "amazon.com"

mydict = {}

for x in mystring:
    if x in mydict.keys():
        mydict[x] += 1
    else:
        mydict[x] = 1

print(mydict)