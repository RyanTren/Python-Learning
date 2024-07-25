# Problem 1
# def is_nested_parens(s):
#     if s == "":
#         return True
#     if len(s) % 2 != 0:
#         return False
#     elif s[0] == '(' and s[-1] == ')':
#         return is_nested_parens(s[1:-1])
#     return False

# s = "(())"
# print(is_nested_parens(s))

# Problem 2
# def count_ones(lst):
#     left = 0
#     right = len(lst) - 1

#     while left <= right:
#         mid = (right + left) // 2
     
#         if lst[mid] == 0:
#             left = mid + 1
#         else: 
#             right = mid - 1

#         if left < len(lst) and lst[left] == 1:
#             return len(lst) - left
#     return 0
        
# lst = [0, 0, 0, 1, 1, 1, 1, 1, 1] # Example Input
# print(count_ones(lst)) # Expected Output: 3

# def binary_search(nums, target):
#     left = 0
#     right = len(nums) - 1
#     mid = (right + left) // 2

#     if left > right: 
#         return -1
#     elif nums[mid] == target:
#       return mid 
#     elif nums[mid] < target:
#       left = mid + 1
#       return binary_search(nums[left:],target)
#     elif nums[mid] > target:
#       right = mid - 1
#       return binary_search(nums[:right], target)

# print(binary_search([1, 3, 5, 7, 9, 11, 13, 15], 11))

# yeah i saw that in java, we put a parameter for left and right, but here we gotta do it differently :/
# the way our teacher taught us this is by changing the amnt of parameters so we can update the values recursively ill just write how i remember it under urs 


def binary_search_two(nums, target, left, right):
    # base case
    if left > right:
        return -1

    mid = (left + right) // 2

    # another base case
    if nums[mid] == target:
        return mid

    # search the left / right side of list how binary search usually does but shorter and kinda faster
    if target < nums[mid]:
        return binary_search_two(nums, target, left, mid -1)
    else:
        return binary_search_two(nums, target, mid + 1, right)

def binary_search_two_recursive(nums, target):
    # this is the initial all to the call back to the binary search function (helper method kidna)
    return binary_search_two(nums, 0, len(nums) - 1, target)

nums = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search_two(nums, 11, 0, len(nums) -1))

# this should work there we go
# dubs