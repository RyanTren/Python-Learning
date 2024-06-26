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

# def binary_search(nums, key):
#     left_idx, right_idx = 0, len(nums) - 1
#     while right_idx >= left_idx:
#         middle_idx = (left_idx + right_idx) // 2
#         if nums[middle_idx] > key:
#             right_idx = middle_idx
#         elif nums[middle_idx] < key:
#             left_idx = middle_idx + 1
#         else:
#             return middle_idx
#     return None

#LC 35 - Search Intert Position is a good one to use for iterative binary search

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left, right = 0, len(nums) - 1
        while right >= left:
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left
        
#good reference: https://www.youtube.com/watch?v=K-RYzDZkzCI

#solution in java:

# class Solution {
#     public int searchInsert(int[] nums, int target) {
#         int left = 0;
#         int right = nums.length - 1;

#         while(left <= right){
#             int middle = (left + right) / 2;
#             if(nums[middle] > target){
#                 right = middle - 1;
#             }
#             else if(nums[middle] < target){
#                 left = middle + 1;
#             }
#             else{
#                 return middle;
#             }
#         }
#         return left;
#     }   
# }

#LC74. Search a 2D Matrix

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or target is None:
            return False

        rows, cols = len(matrix), len(matrix[0])
        low, high = 0, rows * cols - 1
        
        while low <= high:
            mid = (low + high) / 2
            num = matrix[mid / cols][mid % cols]

            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False

# java implementation
# class Solution {
#     public boolean searchMatrix(int[][] matrix, int target) {
#         if (matrix == null || matrix.length == 0) {
#             // Matrix is empty
#             return false;
#         }


#         int row = matrix.length;
#         int cols = matrix[0].length;
#         int low = 0;
#         int high = (row * cols) - 1;

#         while(low <= high){
#             int mid = (low + high) / 2;
#             int num = matrix[mid / cols][mid % cols];

#             if(num == target){
#                 return true;
#             }
#             else if(num < target){
#                 low = mid + 1;
#             }
#             else{
#                 high = mid - 1;
#             }
            
#         }
#         return false;
#     }
# }