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
def max_difference(lst):
  if not lst:
      return 0  # Handle the case when the list is empty
  smallest = min(lst)  # Find the smallest value in the list
  largest = max(lst)   # Find the largest value in the list
  return largest - smallest  # Return the difference between the largest and smallest values

# Example usage:
lst = [5, 22, 8, 10, 2]
max_diff = max_difference(lst)
print(max_diff)  # Output: 20


#Problem 6 Solution
def count_less_than(numbers, threshold):
  count = 0
  for i in range(len(numbers)):
    if numbers[i] < threshold:
      count += 1
  return count  
    
numbers = [12,8,2,4,4,10]
counter = count_less_than(numbers,5)
print(counter) #Output: 3

#Problem 7 Solution
def get_evens(lst):
  new_list = []

  for i in range(len(lst)):
    if lst[i] % 2 == 0:
      new_list.append(lst[i])
  return new_list
  

lst = [1,2,3,4]
evens_lst = get_evens(lst)
print(evens_lst) #Output: [2, 4]

#Problem 8 Solution
def multiples_of_five():
  for i in range(1, 105):
    if(i % 5 == 0):
      print(i)

multiples_of_five() #Output: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100

#Problem 9 Solution
def find_divisors(n):
  new_lst = []

  for i in range(1, n + 1):
    if n % i == 0:
      new_lst.append(i)
  return new_lst

lst = find_divisors(6)
print(lst) #Output: [1, 2, 3, 6]

#Problem 10 Solution
def fizzbuzz(n):
  for i in range(1, n + 1):
    if i % 3 == 0:
      print("Fizz")
    elif i % 5 == 0:
      print("Buzz")
    else:
      print(i)

fizzbuzz(13) #Output: 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13

#Problem 11 Solution


