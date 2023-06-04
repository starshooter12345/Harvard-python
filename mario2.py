"""
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print("#"*size)

main()

"""

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width): #it is better to use different parameters for each function
    print("#"*width) 

main()