def check_palindrome(str):
    str = str.replace(" ", "").lower()
    return str == str[::-1]


str1 = "hello"
str2 = "radar"
str3 = "hi hello hey"

print("str1 is palindrome:", check_palindrome(str1))
print("str2 is palindrome:", check_palindrome(str2))
print("str3 is palindrome:", check_palindrome(str3))
