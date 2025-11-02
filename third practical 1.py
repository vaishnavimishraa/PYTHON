#Practical 3
#Q1.

number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print(f"{number} is divisible by both 3 and 5.")
else:
    print(f"{number} is not divisible by both 3 and 5.")



#Q2.

number = int(input("Enter a number: "))

if number % 5 == 0:
    print(f"{number} is a multiple of 5.")
else:
    print(f"{number} is not a multiple of 5.")

#Q3.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num2} is greater than {num1}")
else:
    print("Numbers are equal.")

#Q4.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

max_num = max(num1, num2, num3)
print(f"The greatest number is: {max_num}")

#Q5.

import cmath

a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    print(f"Real roots: {root1} and {root2}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"Real and equal root: {root}")
else:
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    print(f"Complex roots: {root1} and {root2}")

#Q6.

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    

#Q7.

day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))

#assume 31 days
if day < 31:
    day += 1
else:
    day = 1
    if month < 12:
        month += 1
    else:
        month = 1
        year += 1

print(f"Next date: day={day} month={month} year={year}")

#Q8.

name = input("Name: ")
roll_no = input("Your roll no.: ")
sap_id = int(input("SAP ID: "))
sem = int(input("SEM:"))
course = input("Course: ")
phy = int(input("Physics marks: "))
chem = int(input("Chemistry marks: "))
maths = int(input("Maths marks: "))
pythn = int(input("Python Marks: "))
eng = int(input("English MArks: "))
pds = int(input("PDS Marks: "))
avg = (phy + chem + maths + pythn + eng + pds) / 6
if(avg > 0 and avg < 3.4):
    print("Total CGPA is", avg, "\nYour Overall grade is: F")
elif(avg > 3.5 and avg < 5):
    print("Total CGPA is", avg, "\nYour Overall grade is: C +")
elif(avg > 5.1 and avg < 6):
    print("Total CGPA is", avg, "\nYour Overall grade is: B")
elif(avg > 6.1 and avg < 7):
    print("Total CGPA is", avg, "\nYour Overall grade is: B+")
elif(avg > 7.1 and avg < 8):
    print("Total CGPA is", avg, "\nYour Overall grade is: A")
elif(avg > 8.1 and avg < 9):
    print("Total CGPA is", avg, "\nYour Overall grade is: A+")
elif(avg > 9.1 and avg < 10):
    print("Total CGPA is", avg, "\nYour Overall grade is: O(outstanding)")
    
