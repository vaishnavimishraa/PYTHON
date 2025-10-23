#PRACTICAL NO.4

#Q1

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = int(input("Enter a number: "))
print("The factorial of given number is:", factorial(number))

#Q2

num=int(input("Enter the number:"))
string=str(num)
length=len(string)
arms=0
final=0
for i in string:
    arms=int(i)**length
    final=final+arms
if(final==num):
    print("It is an armstrong number")
else:
    print("It is not an armstrong number")

#Q3

num=int(input("Enter the number:"))
num1=0
num2=1
i=0
while i<=num:
    num3=num1+num2
    i+=1
    print(num3)
    num1=num2
    num2=num3
    
#Q4

def isprime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

number = int(input("Enter a number: "))
if isprime(number):
    print(number, "is a prime number.")
else:
    print(number, "is not a prime number.")

#Q5

def ispalindrome(n):
    original = n
    reverse = 0
    while n > 0:
        digit = n % 10
        reverse = reverse * 10 + digit
        n //= 10
    return original == reverse

n = int(input("Enter a number: "))
if ispalindrome(n):
    print(n, "is a palindrome.")
else:
    print(n, "is not a palindrome.")

#Q6

def sum_of_digits(number):
    sum = 0
    while number > 0:
        digit = number % 10
        sum += digit
        number //= 10
    return sum

number = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(number))

#Q7

count=0
for i in range(1,101):
    if(i%5==0 or i%7==0):
        count+=1
print(count)
    
#Q8

x=input("enter a string:")
if(x.isupper()):
    print(x.lower())
if(x.islower):
    print(x.upper())

#Q9

list = []
for i in range(1,100):
    X = False
    for j in range(2,i):
        if(i%j==0):
            X = True
            break
        else:
            pass
    if X == False:
        list.append(i)
    else:
        pass
print(list)

#Q10

num=int(input("enter any number"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)


