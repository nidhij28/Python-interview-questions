mystr = "Welcome to the world of programming"
sub_str = "welcome"

# if mystr.lower().find(sub_str) == -1:
#     print("substring not found")

# else:
#     print("substring found")

if sub_str in mystr.lower():
    print("substring found")
else:
    print("substring not found")