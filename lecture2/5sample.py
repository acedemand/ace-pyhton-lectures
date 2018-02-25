# recursion functions
# factorial


def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x - 1)


def power(x, y):
    if y == 1:
        return 1
    return x * power(x, y - 1)


print(factorial(5))
print(power(2, 5))
