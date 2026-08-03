mystr = "I have 24 apples 31 bananas and 5 melons"

def extract_nums(str):
    num_list = []
    str_list = mystr.split()
    for element in str_list:
        if element.isdigit():
            num_list.append(element)

    return num_list

result = extract_nums(mystr)
print(result)