a = set()
b = set()

for i in range(10):
    a.add(1)
    b.add(i)
print(a)
print(b)
c = frozenset(b)
#method does not exist c.add()
print(c)
b.add(10)
print(c.union(b))
print(c.intersection(b))

