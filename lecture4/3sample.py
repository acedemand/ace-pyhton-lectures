import random

a = []
b = []
b.extend([None] * 100)

for i in range(100):
    a.append(i)

a.append(random.randint(1, 99))
random.shuffle(a)
print(a)
for i in range(len(a)):
    if b[a[i]] == None:
        b[a[i]] = a[i]
    else:
        print("Duplicate Number is : {}".format(a[i]))
        break
