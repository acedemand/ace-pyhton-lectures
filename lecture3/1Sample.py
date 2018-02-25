try:
  handle = open("1Sample.py")

  for line in handle:
      print (line.rstrip ())

  print("hebele {}".format(handle.read()))
except:
    print("Sth bad happened")


x = range(5)
print(x)