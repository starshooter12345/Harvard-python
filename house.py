"""
name = input("What is your name?")

if name=="Harry" or name=="Hermione" or name=="Ron":
    print("Gryffindor")

elif name=="Draco":
    print("Slytherin")
else:
    print("Who?")

"""

name=input("What is yoour name?")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")