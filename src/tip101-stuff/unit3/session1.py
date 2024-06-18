"""Problem 1"""
def count_mississippi(limit):
  for num in range(1, limit):
    print(f"{num} mississippi")
    
count_mississippi(6)

"""Problem 2"""
def swap_ends(my_str):
  return my_str[-1:] + my_str[1:-1] + my_str[:1]

my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)

"""Problem 3"""
def is_pangram(my_str):
  alphabet = 'abcdefghjklmnopqrstuvwxyz'

  for i in  alphabet:
    if i not in my_str: 
      return False
    return True
  
      
  
my_str = "the quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))

str2 = "The dog jumped"
print(is_pangram(str2))

'''Problem 4'''
def reverse_string(my_str):
  return my_str[::-1]
#start, stop, step

my_str = "live"
print(reverse_string(my_str))

"""Problem 5"""
def first_unique_char(my_str):
  my_dict = {}

  for i in my_str:
    if i in my_dict:
      my_dict[i] += 1
    else:
      my_dict[i] = 1
  
  for k, v in enumerate(my_str):
    if my_dict[v] == 1:
      return k
  return -1

my_str = "leetcode"
print(first_unique_char(my_str))

str2 = "loveleetcode"
print(first_unique_char(str2))

str3 = "aabb"
print(first_unique_char(str3))

str4 = "blahblahhah"

"""Problem 6"""
def min_distance(words, word1, word2):
  index1, index2 = -1, -1
  min_dist = len(words)  # Use the length of the list as the maximum possible distance
  for i, word in enumerate(words):
      if word == word1:
          index1 = i
          if index2 != -1:
              min_dist = min(min_dist, index1 - index2)
      elif word == word2:
          index2 = i
          if index1 != -1:
              min_dist = min(min_dist, index2 - index1)
  return min_dist if min_dist != len(words) else -1

words = ["the", "quick", "brown", "fox", "jumped", "the"]
dist1 = min_distance(words, "quick", "jumped")
dist2 = min_distance(words, "the", "jumped")
print(dist1)
print(dist2)

words2 = ["code", "path", "code", "contribute",  "practice"]
dist3 = min_distance(words, "code", "practice")
print(dist3)
