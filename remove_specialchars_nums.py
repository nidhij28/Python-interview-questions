mystr = "HelloWorld@123"


newstr = "".join(ch for ch in mystr if ch.isalpha())
print(newstr)