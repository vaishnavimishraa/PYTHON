num= int(input("Enter no.:"))
for i in range(2, num):
    if(num%i==0):
        print("not prime")
        break
else:
    print("Prime")