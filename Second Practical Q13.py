#13.	Using membership operator find whether a given character is in a string.
b = "abcdefghijklmnop"
z = "y"
while z == "y":
    a = input("Enter a char: ")
    if(a in b):
        print(a, "is in string")
        z = input("Do u wanna continue?(y/n): ")
    elif(a not in b):
        print(a, "is not in string")
        z = input("Do u wanna continue?(y/n): ")
