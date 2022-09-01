s = input("Enter colour ")    # Question no :- 10
l1 = ("yellow","blue","orange","white","black","red")
for colour in l1:
    if colour in s:
        match colour:
            case "yellow":
                print("Monday")
                break
            case "blue":
                print("Tuesday")
                break
            case "orange":
                print("Wednesday")
                break
            case "white":
                print("Thursday")
                break
            case "black":
                print("Friday")
                break
            case "red":
                print("Saturday")
                break
else:
    print("Sunday")
print()