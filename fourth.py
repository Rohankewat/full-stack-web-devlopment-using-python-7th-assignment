option = int(input("Enter option ")) # Question no :- 3
x = int(input("Enter 1st number "))
y = int(input("Enter 2nd number "))
z = int(input("Enter 3rd number "))
l = x**2
m = y**2
n = z**2
r = l+m 
s = m+n 
t = l+n 

match option:
    case 1:
        if x==y!=z:
            print("isoscles triangle")
        else:
            if y==z!=x:
                print("isosceles triangle")
            else:
                if z==x!=y:
                    print("isosceles triangle")
                else:
                    print("not isoscels triangle")
    case 2:
        if x == y != z:
            print("not right angle triangle")
        elif x == z != y:
            print("not right angle triangle")
        elif y == z != x:
            print("not right angle triangle")
        elif x == y == z:
            print("not right angle triangle")
        elif x>y>z:
            if l==s:
                print("right angle triangle")
            else:
                print("not right angle triangle")
        elif x>z>y:
            if l == s:
                print("right angle triangle")
            else:
                print("not right angle triangle")
        elif z>y>x:
            if n==r:
                print("right angle triangle")
            else:
                print("not right angle triangle")
        elif y>z>x:
            if m==t:
                print("right angle triangle")
            else:
                print("not right angle traingle")
        elif y>x>z:
            if m == t:
                print("right angle triangle")
            else:
                print("not right angle triangle")
        else:
            if z>x>y:
                if n==r:
                    print("right angle triangle")
                else:
                    print("not right angle triangle")
    case 3:
        if x==y==z:
            print("equilateral triangle")
        else:
            print("not equilateral triangle")
    case 4:
        exit()
    case _:
        print("you enter wrong option")
print()