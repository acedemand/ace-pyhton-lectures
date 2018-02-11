def read_file(filePath):
    file = open(filePath)
    for line in file.readlines():
        print(line)
    file.close()


read_file("/home/pamir/dev/projects/pyhton/week2/3sample.py")