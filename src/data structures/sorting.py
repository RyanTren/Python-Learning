#merge sort
"""
Divde and conquer strategy: 
recursively sorts each half of the list
then performs an O(n) merging operation
to create a fully sorted list.
"""

#recursive implementation of merge
def merge(list1, list2):
    if len(list1) == 0:
        return list2
    if len(list2) == 0:
        return list1
    if list1[0] < list2[0]:
        return [list1[0]] + merge(list1[1:], list2)
    else:
        return [list2[0]] + merge(list1, list2[1:])


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    middle_idx = len(nums) // 2
    left_sorted = merge_sort(nums[:middle_idx])
    right_sorted = merge_sort(nums[middle_idx:])
    return merge(left_sorted, right_sorted)
