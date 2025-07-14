# age= int(input("enter age:"))
# if(age>=18):
#     print("yes!")

# else:
#     print("no!")


age= int(input("enter age:"))
if(age%2 ==0):
    print("age is even")

if(age>=18):
    print("yes!")
    print("you can vote!")

elif(age<=0):
    print("Invalid age")

else:
    print("no!")