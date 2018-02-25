a = []
print(dir(a))
for i in range(10):
    a.append("item{}".format(i))

print(a)
print(a.pop())
print(a)


#----------- slicing ----------------#
print("--"*3 + "slicing  " + "--"*3)
x = 'computer'
print("x[1:4] {}".format(x[1:4]))
print("x[1:6:2] {}".format(x[1:6:2]))
print("x[3:] {}".format(x[3:]))
print("x[:5] {}".format(x[:5]))
print("x[-3] {}".format(x[-3]))
print("x[:-2] {}".format(x[:-2]))

print("--"*3 + "enumeration  " + "--"*3)
for i,j in enumerate(a):
    print("{} : {}".format(i,j))

