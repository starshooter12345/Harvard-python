"""
def main():
        print_column(3)

def print_column(height): #height is the parameter we should take in
    print("#\n"*height, end="")

main()

"""

"""
def main():
    print_row(4)

def print_row(width):
    print("?" * width)


main()
"""

def main():
    print_square(3)

def print_square(size): #size is the parameter that corresponds to 3 above
    for i in range(size): #x axis (represents the rows) - for each row in square

        for j in range(size): #y axis(represents the columns)- for each brick in row

            #print brick - brick is the column in this sense
            print("#",end="")#no new line after each column
            #-end operator places all bricks or hashes together in one row
            
        print()#print a new line after each row


main()




