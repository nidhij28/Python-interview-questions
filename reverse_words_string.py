def reverse_str(str):
    str_list = str.split(" ")
    rev_str_list = str_list[::-1]
    return " ".join(rev_str_list)


str = "hello it's a good morning"
print(reverse_str(str))