# import csv
#to read from the csv file
# people = []

# with open("people.csv", newline='') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         people.append(row)

# for person in sorted(people, key=lambda person: person['Name']):
#     print(f"{person['Name']} is from {person['Home']}")


#to write to a csv file
# import csv
# name = input("What's your name?")
# home = input("What's your home?")

# with open("people.csv","a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name,home])


import csv
name = input('What is your name?')
home = input('What is your home?')

with open('people.csv','a') as file:
    writer = csv.DictWriter(file, fieldnames=['name','home'])
    writer.writerow({'name':name,'home':home})



