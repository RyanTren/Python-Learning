#Problem 1
def sum_of_number_string(nums):
  total = 0
  for num in nums:
      total += int(num)
  return total

nums = ["10", "20", "30"]
sum = sum_of_number_string(nums)
print(sum)


#Problem 2
def remove_duplicates(nums):
  new_lst = []
  seen = set()
  for i in nums:
      if i not in seen:
          seen.add(i)
          new_lst.append(i)
  return new_lst

nums = [1,1,1,2,3,4,4,5,6,6]
print(remove_duplicates(nums))


#Problem 3

#Understand
# s = "a-bC-dEf-ghIj"
# Output: j-Ih-gfE-dCba

def reverse_only_letters(s):
  # return s[::-1]

  # Plan
  # 1) make new list to store letters
  # 2) loop thru the string if the letters in the string are alphanumeric, add the letters to the empty list
  # 3) 

  letters = []

  for char in s:
    if char.isalpha():
      letters.append(char)

  result = ""
  letters_index = len(letters) - 1

  for char in s:
    if char.isalpha():
      result += letters[letters_index]
      letters_index -= 1
    else:
      result += char
  return result

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)


# Problem 4
def longest_uniform_substring(s):
  if not s:
    return 0

  maxlenght = 1
  current = 1

  for i in range(1, len(s)):
    if s[i] == s[i - 1]:
      current += 1
      maxlenght = max(maxlenght, current)
    else: 
      current = 1
  return maxlenght

s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1)

s2 = "abcdef"
l2 = longest_uniform_substring(s2)
print(l2)

# Problem 5
def find_poisoned_duration(time_series, duration):
  total_duration = 0

  for i in range(len(time_series) -1):
    # calc the actual poison time between two attacks
    real_duration = min(time_series[i + 1] - time_series [i] - 1, duration)
    total_duration += real_duration

  # this adds the last duration of the attack
  total_duration += duration
  return total_duration


time_series = [1,4,9]

# Plan
"""
1: attack
2: poison
3: poison
4: attack, reset to 3 sec duration
5: poison
6: poison
7: poison
8: poison
9: attack
10: poison
11: poison
12: poison

"""

damage = find_poisoned_duration(time_series, 3)
print(damage)

# Example Output: 8