#5.	Check whether the quadratic equation has real roots or imaginary roots. Display the roots
a = int(input("coefficient of x^2: "))
b = int(input("coefficient of x: "))
c = int(input("constant value: "))

#checking for the nature of roots
# if b^2 - 4ac is > 0 then real roots or if < 0 then imaginary
d = (b**2) - (4 * a * c)
if(d > 0):
    print("Roots are real and distinct")
elif(d == 0):
    print("Roots are real and repeated")
else:
    print("Roots are imaginary")