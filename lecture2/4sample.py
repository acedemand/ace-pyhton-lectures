i = 20

def dump(x, y, name, surname):
    print("x: {}, y: {} name: {} surname: {}".format(x, y, name, surname))


def dump2(x=10, y=12, name="pamir"):
    print("x: {}, y: {} name: {}".format(x, y, name))


def dump3(name,*args):
    print(name)
    for arg in args:
        print(arg)

def scope():
    i = 10
    def inner_scope():
        i = 12
        print("i is {}".format(i))
    inner_scope()
    print("i is {}".format(i))

dump(10, 12, surname="erdem", name="pamir")
dump2(10, 12)
dump2(15)
dump2(y = 15)
dump2(y = 15,name="Taha")
dump3("pamir",12,13,14,15,16,15,18)
scope()
scope()
print("i is {}".format(i))

