list1= ["apple, banana, mango, grapes, orange"]
print(list1)

#to print even numbers between 1 and 100
list4= [x for x in range(0,101,2)]
print(list4)

#to print odd numbers between 1 and 100
list5= [x for x in range(1,101,2)]
print(list5)

list1.append("guava")
print(list1)

list1.extend(["pear, watermelon"])
print(list1)

list1.insert(2, "grapes")
print(list1)

list2= ["apple", "banana", "mango"]
print(list2)

list2.insert(1, "grapes")
print(list2)

list2.remove("apple")
print(list2)

list2.pop(1)
print(list2)

list2.pop(0)
print(list2)

list3= ["red", "green", "blue"]
list3.clear()
print(list3)

list4= ["red" , "pink", "green", "black"]
list4.count(2)
print(list4)

list4= ["red" , "red", "green", "black"]
list4.count(1)
print(list4)

list4.sort()
print(list4)

list4.reverse()
print(list4)

list5= ["yes"]
list4 + list5
print(list4 + list5)

n= list4 * 2
print(n)

list4 [1:3]
print(list4)#dunno

list6= ["red", "pink"]
p= list4 in list6
print(p)

list6= ["red", "green"]
t= list6 in list4
print(t) #dunno

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
[[row[i] for row in matrix] for i in range(4)]
print(matrix)  #not sure








