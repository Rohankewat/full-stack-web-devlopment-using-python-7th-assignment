string1 = input("Enter string ")    # Question no :- 6
string2 = string1.strip()
match string2:
    case string2 if " " in string2:
        print("multiword string")
    case string2 if " " not in string2:
        print("single word string")
print()