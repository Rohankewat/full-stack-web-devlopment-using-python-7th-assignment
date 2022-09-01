number = int(input("Enter number ")) # Question no :- 5
match number:
    case number if number % 2 == 0:
        print("Saurabh shukla")
    case number if number < 0 and number % 2 != 0:
        print("Prateek Jain")
    case number if number > 0 and number % 2 != 0:
        print("Aditya Choudhary")
print()