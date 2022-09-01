print("1 -> Addition")      # Question no :- 2
print("2 -> Subtraction")
print("3 -> Multiplication")
print("4 -> Division")
option = int(input("Select one above operation "))
a,b = int(input("Enter a = ")),int(input("Enter b = "))
match option:
    case 1:
        c= a+b
        print("sum is",c)
    case 2:
        c = a-b
        print("Subtraction is",c)
    case 3:
        c = a*b
        print("Multiplication is",c)
    case 4:
        if b==0:
            print("Invalid division")
        else:
            c = a/b
            print("Division is",c)
    case _:
        print("Invalid option")
print()

    

