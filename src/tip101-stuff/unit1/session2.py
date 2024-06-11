"""
Problem 1: Print List
Write a function print_list() that takes in a list lst as a parameter and prints out each item in the list.

def print_list(lst):
    pass
Example Input: lst = ["squirtle", "gengar", "charizard", "pikachu"]
Example Output:

squirtle
gengar
charizard
pikachu
"""
#Solution to Problem 1
def print_list(lst):

  for i in lst:
    print(i)
  

lst = ["squirtle", "gengar", "charizard", "pikachu"]
print_list(lst)

"""
Problem 2: Print Doubled List
Write a function doubled() that takes in a list of integers lst as a parameter and prints each item in the list multiplied by two.

def doubled(lst):
    pass
Example Input: lst = [1,2,3]
Example Output:

2
4
6
"""

#Solution to Problem 2
def doubled(lst):
  for i in lst:
    print(i * 2)

lst = [1,2,3]
doubled(lst)

"""
Problem 3: Return Doubled List
Modify the function doubled() so that instead of printing the items, it returns a new list of the doubled numbers.

Example Usage:

lst = [1,2,3]
new_lst = doubled(lst)
print(new_lst)
Example Output:

[2, 4, 6]
"""

#Problem 3 Solution
def doubled(lst):
  new_lst = []
  for i in range(len(lst)):
    new_lst.append(lst[i] * 2)

  return new_lst

lst = [1,2,3]
new_lst = doubled(lst)
print(new_lst)

"""
Problem 4: Flip Signs
Write a function flip_sign() that takes in a list of integers lst as a parameter and returns a new list where each number in the original list has been multiplied by -1.

def flip_sign(lst):
    pass
Example Usage:

lst = [1,-2,-3,4]
flipped_lst = flip_sign(lst)
print(flipped_lst)
Example Output:

[-1, 2, 3, -4]
"""

#Problem 4 Solution
def flip_sign(lst):
  flipped_lst = []  # Initialize an empty list to hold the flipped values
  for num in lst:   # Loop through each number in the input list
      flipped_lst.append(-num)  # Flip the sign of the number and append to the new list
  return flipped_lst  # Return the new list with flipped signs
  

lst = [1,-2,-3,4]
flipped_lst = flip_sign(lst)
print(flipped_lst)

#Problem 5 Solution

