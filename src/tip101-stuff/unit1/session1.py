"""
Session 1 Problem Set Vesion 1 (6/4/2024)
"""

# Problem One - Ryan
def hello_world():
  print("Hello World")
hello_world()

# Problem Two - Ryan
def todays_mood():
  mood = "🥱"
  print("Today's mood: " + mood)
todays_mood()

# Problem Three - Kashyap
def print_menu(menu):
  print("Lunch today is: " + menu)
print_menu("🍜")

#Problem Four - Fahmin
def sum(a, b):
  return a + b
print(sum(20,8) * 2)

# Problem Five - Ryan
def product(a, b):
  return a * b

print(product(22, 7))

# Problem Six - Kashyap
def classify_age(age):
  if age < 18:
    return "child"

  return "adult"

output = classify_age(18)
print(output)
output = classify_age(7)
print(output)
output = classify_age(50)
print(output)

# Problem Seven - Fahmin
def what_time_is_it(hour):
  if hour==2:
    return "taco time 🌮"
  elif hour==12:
    return "peanut butter jelly time 🥪"
  else:
    return "nap time 😴"

time = what_time_is_it(2)
print(time)
time = what_time_is_it(7)
print(time)
time = what_time_is_it(12)
print(time)

#Problem 8 - Ryan
def blackjack(score):
  if score == 21:
    print("Blackjack!")
  elif score > 21:
    print("Bust!")
  elif score >= 17 and score < 21:
    print("Nice hand!")
  elif score < 17:
    print("Hit me!")

blackjack(24)
blackjack(19)
blackjack(21)
blackjack(10)

# Problem 9 - Kashyap
def get_first(lst):
  if lst:
    return lst[0]
  return None
print(get_first([3,1,6,7,5]))

# Problem 10 - Fahmin
def get_last(lst):
  if lst:
   return lst[len(lst)-1]
  return None

print(get_last([3,1,6,7,5]))

# Problem 11 - Ryan
def counter(stop):
  for i in range(1, stop+1):
    print(i)

counter(7)

# Problem 12 - Kashyap
def sum_ten():
  sum = 0
  for i in range(1, 11):
    sum = sum + i
  return sum
output = sum_ten()
print(output)

# Problem 13 - Fahmin
def sum_positive_range (stop):
 sum= 0
 for i in range (1,stop+1):
   sum += i
 return sum

sum = sum_positive_range(6)
print(sum)

# Problem 14 - Ryan
def sum_range(start, stop):
  sum = 0
  for i in range(start, stop + 1):
    sum += i
  return sum

print(sum_range(3, 9))


# Problem 15 - Kashyap
def print_negatives(lst):
  for i in range(len(lst)):
    if lst[i] < 0:
      print(lst[i])

print_negatives([3, -2, 2, 1, -5])
