mystr = "hello welcome to the earth"

mystr_list = mystr.split()
result = ""

for word in mystr_list:
    result += word[0]

print(result)