students2 = []
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student={"name":name, "house":house}
        students2.append(student)

#A dictionary is sorted using a key
for student in sorted(students2,key = lambda student:student["name"]):
    print(f"{student['name']} is in {student['house']}")

#lambda is an anonymous function  (no need to create a seperate function to sort the dictionary)  





# import csv
# students = []
# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for name,home in reader:
#         students.append({"name":name,"home":home})

# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")
