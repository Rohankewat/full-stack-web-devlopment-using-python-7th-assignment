year = int(input("Enter a year "))   # Question no :- 9
match year:
    case year if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        print("Century leap year")
    case year if year % 4 == 0 and year % 100 != 0:
        print("Non cetury leap year")
    case year if year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
        print("Century Non leap year")
    case year if year % 4 != 0:
        print("Non century Non leap year")
print()