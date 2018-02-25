largest = None
smallest = None

while True:
    inp = input ("Enter a number: ")
    if inp == "done": break
    try:
        num = float (inp)
    except:
        # print "Please enter a number as input or \'done\'"
        print
        "Invalid input"
        continue
    if smallest is None:
        smallest = num
    if num > largest:
        largest = num
    elif num < smallest:
        smallest = num


def done(largest, smallest):
    print ("Maximum is", int (largest))
    print ("Minimum is", int (smallest))


done (largest, smallest)

try:
    inp = input ("Please enter hours: ")
    hours = float (inp)
    inp = input ("Please enter rate: ")
    rate = float (inp)
except:
    print ("Please enter a number as input")
    quit ()


def computepay(h, r):
    if (h > 40):
        pay = (40 * r) + (h - 40) * 1.5 * r
    else:
        pay = (h * r)
    return pay


print (computepay (hours, rate))
