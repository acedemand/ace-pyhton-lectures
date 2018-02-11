student = {
    "name":"Pamir",
    "id": "2010186003"
}
try:
    last_name = student["last_name"]
    print(last_name)
except KeyError as error:
    print("Exception handled")
    print(error)
