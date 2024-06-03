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


# Quick sort (O(n^2) worse case, O(nlogn) average case, O(logn) space complexity

def partition(nums, left_idx, right_idx):
    pivot = nums[left_idx]
    while True:
        while nums[left_idx] < pivot and left_idx <= right_idx:
            left_idx += 1
        while nums[right_idx] > pivot and right_idx >= left_idx:
            right_idx -= 1
        if left_idx >= right_idx:
            return right_idx
        nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]
        left_idx += 1
        right_idx -= 1



def quick_sort_helper(nums, left_idx, right_idx):
    if left_idx >= right_idx:
        return
    pivot_idx = partition(nums, left_idx, right_idx)
    if left_idx < pivot_idx - 1:
        quick_sort_helper(nums, left_idx, pivot_idx)
    if right_idx > pivot_idx + 1:
        quick_sort_helper(nums, pivot_idx + 1, right_idx)

def quick_sort(nums):
    quick_sort_helper(nums, 0, len(nums) - 1)