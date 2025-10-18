a = 15
b = 12

# Adding two numbers
res = a + b
print(res)


text = input("Enter a word or number: ")
text = text.lower()
reversed_text = text[::-1]

if text == reversed_text:
    print("It is a palindrome!")
else:
    print("It is not a palindrome.")
