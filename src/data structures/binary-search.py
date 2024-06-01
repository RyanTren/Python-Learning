#used to locate an element in a sorted list
#done in O(n) time but optimization speeds it up to O(log n)
#good to use on arrays

#bs is a recursive algorithm
"""finds middle element in list and then 
recursivly searches the left or right side 
of the list"""


#recursive binary search
"""
The recursive approach utilizes a helper function to 
keep track of pointers to the section of the list we 
are currently examining. The search either terminates 
when we find the key or if the two pointers meet.
"""

def binary_search(nums, key):
    return recursive_binary_search(nums, key, 0, len(nums))

def recursive_binary_search(nums, key, start_idx, end_idx):
    middle_idx = (start_idx + end_idx) // 2
    if start_idx == end_idx:
        return None
    if nums[middle_idx] > key:
        return recursive_binary_search(nums, key, start_idx, middle_idx) #left side of list
    elif nums[middle_idx] < key:
        return recursive_binary_search(nums, key, middle_idx + 1, end_idx) #right side of list
    else:
        return middle_idx

#iterative binary search
"""
The iterative approach manually keeps track of the 
section of the list we are examining using the 
two-pointer technique. The search either terminates 
when we find the key, or the two pointers meet.
"""

def binary_search(nums, key):
    left_idx, right_idx = 0, len(nums)
    while right_idx > left_idx:
        middle_idx = (left_idx + right_idx) // 2
        if nums[middle_idx] > key:
            right_idx = middle_idx
        elif nums[middle_idx] < key:
            left_idx = middle_idx + 1
        else:
            return middle_idx
    return None