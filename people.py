import csv

people = []

with open("people.csv", newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        people.append(row)

for person in sorted(people, key=lambda person: person['Name']):
    print(f"{person['Name']} is from {person['Home']}")
