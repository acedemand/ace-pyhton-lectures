def add_numbers(a, b):
    return (a * b) + a


def fibonacci(a):
    if a == 1 or a == 0:
        return 1
    return fibonacci (a - 1) + fibonacci (a - 2)


print(add_numbers(2, 3))
print(fibonacci(6))
