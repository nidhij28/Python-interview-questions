def generate_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


print(generate_factorial(5))