"""with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")  # Split the line into separate values using ","
        print(f"{name} is in {house}")"""

"""students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)"""

students = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student={"name":name, "house":house}
        students.append(student)

def get_name(student):
    return student["name"]

#A dictionary is sorted using a key
for student in sorted(students,key = get_name, reverse=True):
    print(f"{student['name']} is in {student['house']}")

    #The list of dictionaries is sorted using get_name
    #In this case, the list has many dictionaries

    #we can also use get_house as the sorting key

    #by default the sort function sorts in ascending order but reverse=True sorts in descending order based on the get_name key

#a dictionary is inside a list