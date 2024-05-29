print('hello')

print(5 + 2)

x = 'hellow world'
print(x)

if 5 > 2:
    print('5 is greater than 2')
else:
    print('5 is not greater than 2')

#This is a comment

"""
This 
is a 
block comment
"""


carname = "Volvo"
x = 50

x = 5
y = 10
z = x + y
print(z)

x, y, z = "Orange", "Banana", "Cherry"
x = y = z = "Orange"


def myFunc():
    global x
    x = "fantastic"

x = 5
print(type(x))
#int

x = "Hello World"
print(type(x))
#str

x = 20.5
print(type(x))
#float

x = ["apple", "banana", "cherry"]
print(type(x))
#list

x = ("apple", "banana", "cherry")
print(type(x))  
#tuple

x = {"name" : "John", "age" : 36}
print(type(x))
#dict

x = True    
print(type(x))
#bool

x = 5
x = float(x)

x = 5.5
x = int(x)

x = 5
x = complex(x)

x = "Hello World"
print(len(x))

txt = "Hello World"
x = txt[0]

#Get the characters from index 2 to index 4 (llo).
txt = "Hello World"
x = txt[2:5]

#Return the string without any whitespace at the beginning or the end.
txt = " Hello World "
x = txt.strip()

#Convert the value of txt to upper case.
txt = "Hello World"
x = txt.upper()

#Convert the value of txt to lower case.
txt = "Hello World"
x = txt.lower()

#Replace the character H with a J.
txt = "Hello World"
x = txt.replace("H", "J")

#Insert the correct syntax to add a placeholder for the age parameter.
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#Use the correct membership operator to check if "apple" is present in the fruits object.

fruits = ["apple", "banana"]
if "apple" in fruits:
    print("Yes, apple is a fruit!")

#Use the correct comparison operator to check if 5 is not equal to 10.
if 5 != 10:
    print("5 and 10 is not equal")

#Use the correct logical operator to check if at least one of two statements is True.
if 5== 10 or 4 == 4:
    print("At least one of the statements is true")

#Print the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
print(fruits[1])

#Change the value from "apple" to "kiwi", in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

#Use the append method to add "orange" to the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#Use the insert method to add "lemon" as the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

#Use the remove method to remove "banana" from the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#Use negative indexing to print the last item in the list.
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#Use a range of indexes to print the third, fourth, and fifth item in the list.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#Use the correct syntax to print the number of items in the list.
fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#Use the correct syntax to print the first item in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(fruits[0])

#Use the correct syntax to print the number of items in the fruits tuple.
fruits = ("apple", "banana", "cherry")
print(len(fruits))

#Use the correct syntax to print the first item in the fruits set.
fruits = {"apple", "banana", "cherry"}
for x in fruits:
    print(x)
    break

#Use the correct syntax to add "orange" to the fruits set.
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")



