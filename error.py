#1
''''num= int(input("enter the numerator:"))
deno= int(input("enter thr denominator:"))
try:
    quo= num/deno
    print("QUOTIENT: ", quo)
except ZeroDivisionError:
        print("denominator cannot be zero")'''

#2
try:
    num= int(input("enter the number:"))
    print(num**2)
except (KeyboardInterrupt):
    print("you should have entered a number..... Program Terminating...")
except(ValueError):
    print("please check before you enter..... Program Terminating...")
print("Bye")

#3
try:
    file = pen('File1.txt')
    str= f.readline()
    print(str)
except    
