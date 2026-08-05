mystring1 = "listen"
mystring2 = "silent"

if sorted(mystring1.lower()) == sorted(mystring2.lower()):
    print("strings are anagrams")
else:
    print("strings are not anagrams")