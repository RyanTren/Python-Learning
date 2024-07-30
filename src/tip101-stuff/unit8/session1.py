# Problem 1
# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# root = TreeNode(10)
# root.left = TreeNode(4)
# root.right = TreeNode(6)

# Problem 2
# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def check_tree(root):
#     if root.left.val + root.right.val == root.val:
#         return True
#     return False

'''root = TreeNode(5)
root.left = TreeNode(3)
#root.right = TreeNode(1)
print(check_tree(root))'''


"""
Example Input Tree #1: 
  10
 /  \
4    6
Input: root = 10
Expected Output: True

Example Input Tree #2: 
  5
 / \
3   1
Input: root = 5
Expected Output: False
"""

# Problem 3
# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def check_tree(root):
#     if not root:
#         return False
#     if not root.right:
#         if root.val == root.left.val:
#             return True
#     elif not root.left:
#         if root.val == root.right.val:
#             return True
#     else:
#         if root.left.val + root.right.val ==root.val:
#             return True
#     return False
    

# root = TreeNode(5)
# root.left = TreeNode(3)
# # root.right = TreeNode(1)
# print(check_tree(root))

"""
Example Input Tree #1: 
  10
 /  
10    
Input: root = 10
Expected Output: True

Example Input Tree #2: 
  5
 / \
3   2
Input: root = 5
Expected Output: True

Example Input Tree #3: 
  5
   \
    2
Input: root = 5
Expected Output: False

Example Input Tree #4: 
Empty Tree (None)
Input: root = None
Expected Output: False
"""

# Problem 4
# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def left_most(root):
#     '''while root.left:
#         root = root.left
#     return root.val'''

#     if root is None:
#         return None
#     if root.left is None:
#         return root.val

#     return left_most(root.left)


# root = TreeNode(1)
# #root.left = TreeNode(2)
# root.right = TreeNode(2)
# root.right.left = TreeNode(3)
# #root.left.left = TreeNode(4)
# #root.left.right = TreeNode(3)
# print(left_most(root))

"""
Example Input Tree #1: 

      1
     / \
    /   \
   2     5
  / \    
 4   3    

Input: root = 1
Expected Output: 4

Example Input Tree #2: 

     1
      \
       2
      / 
     3    

Input: root = 1
Expected Output: 1

Example Input Tree #3: 

Input: root = None
Output: None
"""

# Problem 5
# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def left_most(root):
#     if root is None:
#         return None
#     if root.left is None:
#         return root.val
    
#     return left_most(root.left)

# root = TreeNode(1)
# # root.left = TreeNode(None)
# root.right = TreeNode(2)
# # root.right.right = TreeNode(5)
# # root.left.left = TreeNode(2)
# # root.left.left = TreeNode(4)
# # root.left.right = TreeNode(3)
# root.right.right = TreeNode(3)
# print(left_most(root))

"""
Example Input Tree #1: 

      1
     / \
    /   \
   2     5
  / \    
 4   3    

Input: root = 1
Expected Output: 4

Example Input Tree #2: 

     1
      \
       2
      / 
     3    

Input: root = 1
Expected Output: 1

Example Input Tree #3:

Input: root = None
Output: None

"""

# Problem 6
# class TreeNode():
#      def __init__(self, val, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right

# def inorder_helper(current_node, values):
#     if not current_node:
#         return values
#     inorder_helper(current_node.left, values) #left subtree
#     values.append(current_node.val)
#     inorder_helper(current_node.right, values) 
#     return values

# def inorder_traversal(root):
#     value = [] 
#     return inorder_helper(root, value)


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.right.left = TreeNode(4)
# print(inorder_traversal(root))


"""
Example Input Tree #1: 
     1
      \
       2
      / 
     3    

Input: root = 1
Expected Output: [1,3,2]

Example Input Tree #2 : 

Input: root = None
Output: []

Example Input Tree #3:
    1  

Input: root = 1
Output: [1]
"""

# Problem 7
# class TreeNode():
#      def __init__(self, val, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right

# def size(root):
#     if root is None:
#         return 0
#     return 1 + size(root.left) + size(root.right)

# root = TreeNode(4)
# root.left = TreeNode(2)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)
# root.right = TreeNode(5)

# # root = None   
# print(size(root))


"""
Example Input Tree #1: 

      4
     / \
    /   \
   2     5
  / \    
 1   3    

Input: root = 4
Expected Output: 5

Example Input Tree #2: 

Empty tree (None)
Input: root = None
Expected Output: 0
"""

# Problem 8
class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def find(root, value):
    if root is None:
        return False
    if root.val == value:
        return True
        
    return find(root.left, value) or find(root.right, value)
    
# it checks the left first to see if it's there and in the case that it isn't it checks the right which is why we have "or"

    
# Example Input Tree #1: 

#       1
#      / \
#     /   \
#    2     5
#   / \    
#  4   3    

# Input: root = 1, value = 5
# Expected Output: True

# Example Input Tree #2: 

#       1
#      / \
#     /   \
#    2     5
#   / \    
#  4   3    

# Input: root = 1, value = 10
# Expected Output: False