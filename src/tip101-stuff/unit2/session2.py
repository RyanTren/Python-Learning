# Problem 1
def cast_vote(votes, candidate):
  if candidate in votes:
    votes[candidate] += 1
  else:
    votes[candidate] = 1
  return votes


votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)

cast_vote(votes, "Gina")
print(votes)

#Given a dictionary tasks where keys are task names and values are priorities (1-10, where 10 is the highest priority), write a function get_highest_priority_task() that removes the task with the highest priority from the dictionary and returns its name.
#If two tasks have the same priority, return the task that comes first in the alphabet.# Problem 2
def common_keys(dict1, dict2):
  new_lst = []

  for key in dict1:
    if key in dict2:
      new_lst.append(key)
      
  return new_lst

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)

# Problem 3
def get_highest_priority_task(tasks):
  # if not tasks:
  #   return None
  
  highest_task = None
  # highest_priority = max(task.values())
  highest_priority = 0
  
  for task, priority in tasks.items():
    if priority == highest_priority:
      highest_priority = priority
      highest_priority_task = task
      if highest_task is None or task < highest_task:
        highest_task = task
  # tasks.pop(highest_task)
  return highest_task
      


tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

perform_task = (get_highest_priority_task(tasks))
print(perform_task)

print(tasks)




# Problem 4
#Write a function that takes in a list of integers nums and counts the number of occurrences of each integer. The function returns the result as a dictionary with integers as keys and their counts as values.
def count_occurrences(nums):
  new_dict = {}
  
  for num in nums:
    if num in new_dict:
      new_dict[num] += 1
    else:
      new_dict[num] = 1
  return new_dict

nums = [1, 2, 2, 3, 3, 3, 4]
print(count_occurrences(nums))

#Problem 5
#Write a function find_majority_element() that takes in a list of integers elements and finds the majority element in the list. A majority element is an element that appears more than n/2 times where n is the size of the list. If there is no majority element, return None


def find_majority_element(elements):
  count_dict = {}
  for num in elements:
    if num in count_dict:
      count_dict[num] += 1
    else:
      count_dict[num] = 1
  
    if count_dict[num] > len(elements) / 2:
      return num  
  return None

elements = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(elements)) #Output: 2