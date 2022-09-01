age = int(input("Enter age "))   # Question no :- 4
match age:
    case age if 0 <= age <10:
        print("Kid")
    case age if 10 <= age <20:
        print("Teen")
    case age if 20 <= age < 40:
        print("Young")
    case age if 40 <= age < 60:
        print("Experienced")
    case age if 60 <= age <= 100:
        print("Senior citizen")
    case _:
        print("you enter wrong age")
print()
