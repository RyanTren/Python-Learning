# def is_prime(n):
#   if n <= 1:
#     return False

#   if n == 2:
#     return True

#   d = 2

#   while d * d <= n:
#     if n % d == 0:
#       return False
#     d += 1
#   return True
  
# print(is_prime(5))
# print(is_prime(12))
# print(is_prime(9))


# print("\nProblem 2")
# def reverse_list1(lst):
#   left = 0
#   right = len(lst) -1
  
#   while left < right:
#     temp = lst[left]
#     lst[left] = lst[right]
#     lst[right] = temp
    
#     left += 1
#     right -= 1
#   return lst
    
# lst = [1, 2, 3, 4, 5]
# print(reverse_list1(lst))

# print("\nProblem 3")
# def reverse_list(lst):
# # Create a new reversed list


#   print("\nProblem 4: : Move Even Integers")
  #   Problem 4: Move Even Integers
#   Write a function sort_list_by_parity() that takes in an integer list nums as a parameter and moves all the even integers at the beginning of the list followed by all the odd integers. The function returns any list that satisfies this condition.

  # def sort_array_by_parity(nums):
  #     pass
  # # Example Usage:

  # nums = [3,1,2,4]
  # nums2 = [0]
  # print(sort_array_by_parity(nums))
  # print(sort_array_by_parity(nums2))

#   Example Output:

#   [2,4,3,1]
#   # Additional acceptable outputs are [4,2,3,1], [2,4,1,3], and [4,2,1,3]
#   [0]
# # Copy the elements back into the original list
#   for i in range(len(lst)): 
#     lst[i] = reversed_lst[i]
#     return lst

# lst = [1, 2, 3, 4, 5]
# print(reverse_list(lst))

def sort_array_by_parity(nums):
  # create a new list
  # traverse nums
  # for each number check if even, add to new list
  # how do we know that the rest of numbers are odd?

  '''new_nums=[]
  
  for num in nums:
    if num%2==0:
      new_nums.append(num)
  
  for num1 in nums:
    if num1%2==1:
      new_nums.append(num1)

  return new_nums'''

  left = 0
  right = len(nums) -1
  
  while left < right:
    if nums[left] % 2 == 0:
      left += 1
    else:
      temp = nums[left]
      nums[left] = nums[right]
      nums[right] = temp

    if nums[right] % 2 == 1:
      right -= 1
    else:
      temp = nums[right]
      nums[right] = nums[left]
      nums[left] = temp
      
  return nums
  
nums = [3,1,2,4]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))
