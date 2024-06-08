# #Problem 1
def is_subsequence(lst, sequence):
  for i in range(len(lst)):
    if sequence[i] in lst:
      return True
    else:
      return False

lst = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
print(is_subsequence(lst, sequence))


#Problem 2
def create_dictionary(keys, values):
  counter = 0
  new_dict = {}
  
  for i in values:
    if i not in new_dict:
      new_dict[keys[counter]] = i
      counter += 1

  return new_dict

keys = ["peanut", "dragon", "star", "pop", "space"]
values = ["butter", "fly", "fish", "corn", "ship"]
print(create_dictionary(keys,values))

# Problem 3
def print_pair(dictionay, target):
    if target in dictionary:
      print(target)
      print(dictionary[target])
    else:
      print("That pair does not exist!")


dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")

#Expected Output
# Key: patrick
# Value: star
# That pair does not exist!
# Key: spongebob
# Value: squarepants

# Problem 4
def keys_v_values(dictionary):
  sum_keys = 0
  sum_values = 0

  for k, v in dictionary.items():
    sum_keys += k
    sum_values += v

  if sum_keys > sum_values:
    return "keys"
  elif sum_keys < sum_values:
    return "values"
  else:
    return "balanced"

dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
greater_sum = keys_v_values(dictionary1)
print(greater_sum)  # Output should be "values"

dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
greater_sum = keys_v_values(dictionary2)
print(greater_sum)  # Output should be "keys"