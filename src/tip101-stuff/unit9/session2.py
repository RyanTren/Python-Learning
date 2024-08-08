# from typing import Deque

# class TreeNode:
#   def __init__(self, value=0, left=None, right=None):
#       self.val = value
#       self.left = left
#       self.right = right

# def level_order(root):
#   # If the tree is empty:
#   # return an empty list
#   if root is None:
#     return []

#   # Create an empty queue using deque
#   queue = Deque()

#   # Create an empty list to store the explored nodes
#   visited = []

#   # Add the root to the queue
#   queue.append(root)
#   # While the queue is not empty:
#   while queue:
#     # Pop the next node off the queue (pop from the left side!)
#     current_node = queue.popleft()
#     # Add the popped node to the list of explored nodes
#     visited.append(current_node.val)
#     # Add each of the popped node's children to the end of the queue
#     if current_node.left is not None:
#       queue.append(current_node.left) #add left child to queue

#     if current_node.right is not None:
#       queue.append(current_node.right) #add right child to queue
#   # Return the list of visited nodes
#   return visited

# root = TreeNode(4)
# root.left = TreeNode(2)
# root.right = TreeNode(6)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)

# print(level_order(root))

# """
# Example Input Tree:

#       4
#      / \
#     2   6
#    / \
#   1   3

# Example Input: root = 4
# Expected Output: [4, 2, 6, 1, 3]
# Explanation:
# Level 1: Node 4
# Level 2 (left to right): Node 2, Node 6
# Level 3 (left to right): Node 1, Node 3
# """

#Problem 2

# from collections import deque


# class TreeNode:

#   def __init__(self, value=0, left=None, right=None):
#     self.val = value
#     self.left = left
#     self.right = right


# def min_depth(root):
#   if not root:
#     return 0

#   queue = deque()
#   queue.append((root))
#   depth = 1

#   while queue:
#     level = len(queue)
#     # for i in range(level):
#     current = queue.popleft()
#     if current.left is None and current.right is None:
#       return depth
#     if current.left:
#       queue.append(current.left)
#     if current.right:
#       queue.append(current.right)
#     depth = depth +1

#   # return depth


# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(7)
# print(min_depth(root))  # Test case 1

# root2 = TreeNode(2)
# root2.right = TreeNode(3)
# root2.right.right = TreeNode(4)
# root2.right.right.right = TreeNode(5)
# root2.right.right.right.right = TreeNode(6)

# print(min_depth(root2))




# from collections import deque

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def min_depth(root):
#     if not root:
#         return 0

#     queue = deque()  # The queue stores tuples of (node, depth)
#     queue.append((root, 1))

#     while queue:
#         node, depth = queue.popleft()

#         # Check if the current node is a leaf node
#         if not node.left and not node.right:
#             return depth

#         # Add the left child to the queue if it exists
#         if node.left:
#             queue.append((node.left, depth + 1))

#         # Add the right child to the queue if it exists
#         if node.right:
#             queue.append((node.right, depth + 1))

#     return 0  # This line will never be reached if the input tree is valid


# """
# Example Input Tree #1:

#    3
#   / \
#  9  20
#     / \  
#    15  7

# Example Input: root = 3
# Expected Output: 2
# Shortest path from root node to a leaf node is 3 -> 9. Number of nodes in path is 2.

# Example Input Tree #2:

#    2
#     \
#      3
#       \
#        4
#         \
#          5
#           \
#            6        

# Example Input: root = 2
# Expected Output: 5
# Shortest path from root node to a leaf node is 2 -> 3 -> 4 -> 5 -> 6.
# Number of nodes in path is 5.
# """
# Problem 3
from collections import deque

class TreeNode:
  def __init__(self, value=0, left=None, right=None):
      self.val = value
      self.left = left
      self.right = right

def level_difference(root):
      if not root:
          return 0

      queue = deque() 
      queue.append((root))
      evensum=0
      oddsum=0
      counter= 1

      while queue:
          node, depth = queue.popleft()
        
          # Add the left child to the queue if it exists
          if node.left:
              queue.append((node.left))
              if counter % 2 == 0:
                evensum = evensum + node.left.val
              else:
                oddsum = oddsum + node.left.val
        

          # Add the right child to the queue if it exists
          if node.right:
              queue.append((node.right))
              if counter % 2 == 0:
                evensum = evensum + node.left.val
              else:
                oddsum = oddsum + node.left.val
        
          counter = counter+1

        
      return evensum - oddsum




# Create the tree nodes
node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

# Connect the nodes as per the given tree structure
root = TreeNode(6)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(5)
root.right.left = TreeNode(4)
root.right.right = TreeNode(2)
root.right.left.left = TreeNode(1)
root.right.left.right = TreeNode(7)
root.right.right.right = TreeNode(3)

root = node1


print(level_difference(root))




"""
Example Input Tree
          6
         / \
        3   8
       /   / \  
      5   4   2
         / \   \
        1   7   3

      
Expected Output: -5
Explanation: 
Odd level sum: 6 + 5 + 4 + 2 = 17
Even level sum: 3 + 8 + 1 + 7 + 3 = 22
Odd level sum - even level sum: 17 - 22 = -5
"""