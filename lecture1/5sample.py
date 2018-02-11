student_names = ["Pamir", "Erdem", "Nazli", "Naz"]
for name in student_names:
    print ('Name of the student is {0}'.format(name))

for index in range(len(student_names)):
    if student_names[index] == "Erdem":
        break
    print(student_names[index])