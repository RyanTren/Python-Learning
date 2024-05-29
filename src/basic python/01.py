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



