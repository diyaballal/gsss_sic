def x_shape(n):

    for i in range(n):
        for j in range(n):
            if j == i or j == n - i - 1:
                print("*", end =" ")
            else:
                print(" ", end =" ")
        print()


def hollow_square(n):
    
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1 :
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def x_in_hollow_square(n):
    for i in range(n):
        for j in range(n):
            if j == i or j == n-i-1 or i == 0 or i == n-1 or j == 0 or j == n-1 :
                print("*",end=" ")
            else:
                print(" ",end =" ")
        print()


def pascal_triangle(n):
    for i in range(n):                          
        print(" " * (n - i), end="")             
        num = 1                                 
        for j in range(i + 1):                   
            print(num, end=" ")                  
            num = num * (i - j) // (j + 1)       
        print()                                 



def rhombus(n):
    for i in range(n):
        print(" "  * ( n - i - 1 ) + "*" * n )
    print()


while True:
    print("\nChoose a shape:")
    print("1. X Shape")
    print("2. Hollow Square")
    print("3. X inside Hollow Square")
    print("4. Pascal Triangle")
    print("5. Rhombus")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "6":
        break

    n = int(input("Enter no. of lines: "))

    if choice == "1":
        x_shape(n)
    elif choice == "2":
        hollow_square(n)
    elif choice == "3":
        x_in_hollow_square(n)
    elif choice == "4":
        pascal_triangle(n)
    elif choice == "5":
        rhombus(n)
    else:
        print("Invalid choice! Try again.")




