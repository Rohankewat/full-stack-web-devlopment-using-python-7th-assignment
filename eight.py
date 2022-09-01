number = int(input("Enter number "))   # Question no :- 7
match number:
    case number if number < 0:
        print("negative number")
    case number if number > 0:
        print("positive number")
    case number if number == 0:
        print("zero")
print()