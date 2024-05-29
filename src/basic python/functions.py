#Create a function named my_function.
def my_function():
    print("Hello from a function")

#Execute a function named my_function.
my_function()

#Inside the function, add a parameter: fname.
def my_function(fname):
    print(fname + " Refsnes")

#Let the function return the x parameter + 5.
def my_function(x):
    return x + 5

#If you do not know the number of arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix is *.
def my_function(*kids):
    print("The youngest child is " + kids[2])

#If you do not know the number of keyword arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix is **.
def my_function(**kid):
    print("His last name is " + kid["lname"])
