"""
try:
    x=int(input("What's x? "))
    
except ValueError:
    print("x is not an integer")

else:
    print(f"x is {x}")
"""
"""
#below code loops till the user enters an integer
while True:
    try:
        x=int(input("What is x?"))
    except ValueError:
        print("x is not an integer")
    else:
        break #stops the program after the necessary input is entered and outputted

print(f"x is {x}")
"""

"""
#an alternative:

while True:
    try:
        x=int(input("What is x?"))
        break #stops the program after the necessary input is entered and outputted
    except ValueError:
        print("x is not an integer")
   
        

print(f"x is {x}")

"""

"""
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("What is x?"))
        except ValueError:
            print("x is not an integer")
        else:
            break  # Stops the program after the necessary input is entered and outputted

    return x

main()

"""

"""
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input("What is x?"))
        except ValueError:
           # print("x is not an integer")
         # Stops the program after the necessary input is entered and outputted
            pass


main()
"""

#considering code reusability
def main():
    x = get_int("What's x?")
    print(f"x is {x}")

def get_int():
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()




