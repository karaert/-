name = "Vlad"
secondName = "Tkachuk"
age =  16
fullName = name + " " + secondName
list = [fullName]

if type(name) == type(secondName):
    print(f"type: {type(name)}")
else:
    print("ERROR")

if type(age) == int:
    print(type(age))
    print(list[0])
else:
    print("ERROR")
