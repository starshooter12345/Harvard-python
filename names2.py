
""""
name = input("What's your name? ")

The below line opens and closes the file at the same time

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
"""

with open("names.txt") as file:
    for line in sorted(file):
        print("hello,",line.rstrip())
