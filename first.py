month = int(input("Enter month no ")) # Question no :- 1

match month:
    case 1:
        print("number of days in JANUARY are 31")
    case 2:
        print("number of days in FEBRUARY are 28")
    case 3:
        print("number of days in MARCH are 31")
    case 4:
        print("number of days in APRIL are 31")
    case 5:
        print("number of days in MAY are 31")
    case 6:
        print("number of days in JUNE are 30")
    case 7:
        print("number of days in JULY are 31")
    case 8:
        print("number of days in AUGUST are 31")
    case 9:
        print("number of days in SEPTEMBER are 30")
    case 10:
        print("number of days in OCTOBER are 31")
    case 11:
        print("number of days in NOVEMBER are 30")
    case 12:
        print("number of days in DECEMBER are 31")
    case _:
        print("you enter wrong month")
print()