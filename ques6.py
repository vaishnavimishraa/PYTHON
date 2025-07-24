#4!= 1x2x3x4
num= int(input("enter:"))
factorial=1
for i in range(1,num+1):
    factorial= factorial * i 
print(f"Factorial of {num} is {factorial}")