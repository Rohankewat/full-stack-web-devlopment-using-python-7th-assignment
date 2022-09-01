s1 = input("Enter first string ")     # Question no :- 8
s2 = input("Enter second string ")
match (s1,s2):
    case (s1,s2) if s1 == s2:
        print("both strings are identical")
    case (s1,s2) if s1>s2:
        print("{} comes after {} in dictionary".format(s1,s2))
    case (s1,s2) if s1<s2:
        print("{} comes after {} in dictionary".format(s2,s1))
print()