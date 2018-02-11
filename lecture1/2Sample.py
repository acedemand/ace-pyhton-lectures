def add_numbers(a, b):
    print(a + b)


# add two numbers and returns it
def add_numbers2(a: int, b: int) -> int:
    c = int(a)
    d = int(b)
    return c + d


print(add_numbers2(3, 5))
