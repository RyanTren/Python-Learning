#Problem Node
# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = value
#          self.left = left
#          self.right = right

# Plan
# first make the helper method that check if the current node has the same value of the other nodes in the BST
#   base case:   if not node return true
#    if node.val != value return false
# return is_univalued(node.left, value) and is_univalued(node.right, value)

# main method
# if not root return True
# return is_univalued_helper(root, root.val)



# def is_univalued_helper(node, value):
#     if not node:
#         return True
#     if node.val != value:
#         return False
#     return is_univalued_helper(node.left, value) and is_univalued_helper(node.right, value)

# def is_univalued(root):
#     if not root:
#         return True
#     return is_univalued_helper(root, root.val)


# root = TreeNode(1, TreeNode(1, TreeNode(2, TreeNode(1, TreeNode(1, TreeNode(1))))))
# print(is_univalued(root))

"""
Example Input Tree #1

      1
     / \
    /   \
   1     1
  / \     \
 1   1     1

Input: root = 1
Expected Output: True

Example Input Tree #2

      1
     / \
    /   \
   1     2
  / \     \
 1   1     1

Input: root = 1
Expected Output: False
"""

# Problem 2
# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = value
#          self.left = left
#          self.right = right

# def height(root):
#     if root is None:
#         return 0

#     left_side = height(root.left)
#     right_side = height(root.right)

#     return max(left_side, right_side) + 1

# root = TreeNode(4)
# # root.left = TreeNode(2)
# # root.right = TreeNode(5)
# # root.left.left = TreeNode(1)
# # root.left.right = TreeNode(3)
# print(height(root))

"""
Example Input Tree #1

      4
     / \
    /   \
   2     5
  / \    
 1   3    

Input: root = 4
Expected Output: 3

Example Input Tree #2 

      4 

Input: root = 4
Expected Output: 1
"""

# Problem 3
# class TreeNode():
#      def __init__(self, key, value, left=None, right=None):
#          self.key = key
#          self.val = value
#          self.left = left
#          self.right = right

# def insert(root, key, value):

#plan
#base if the tree is empty, create a new node
#check if key exists. if yes, update root.key == key
#compare smaller and bigger and callr ecursively 
#return the root

#     if not root:
#         return TreeNode(key, value)

#     if root.key == key:
#         root.val = value
#     elif key > root.key:
#         root.right = insert(root.right, key, value)
#     elif key < root.key:
#         root.left = insert(root.left, key, value)

#     return root
    

# root = TreeNode(10, 'Naruto')
# root.left = TreeNode(8, 'a')
# root.right = TreeNode(15, 'b')
# root.left.left = TreeNode(1, 'c')
# root.left.right = TreeNode(6, 'd')

# key = 9
# value = 'Naruto'

# node = insert(root, key, value)

# def preorder(node):
#     if node is not None:
#         print(node.key)
#         preorder(node.left)
#         preorder(node.right)

# preorder(node)

"""
Example Input Tree #1: (tree depicted using keys)

      10
     /  \
    /    \
   8      15
  / \    
 1   6    

Input: root = 10, key = 9, value = 'Naruto' 
Expected Output: root = 10


Expected Output Tree:

      10
     /  \
    /    \
   8      15
  / \    
 1   6
      \
       9    


Example Input Tree #2: Empty Tree (None)

Input: root = None, key = 4, value = "Sailor Moon"
Expected Output: root = 4


Expected Output Tree:

      4
"""

# Problem 4
class TreeNode():
     def __init__(self, key, value, left=None, right=None):
         self.key = key
         self.val = value
         self.left = left
         self.right = right

def remove_bst(root, key):
    # Locate the node to be removed
    # If the node is a leaf node:
        # Remove the node by redirecting the appropriate child reference of its parent to None
    # If the node has one parent:
        # Replace the node with its child, updating its parent's nodes child reference appropriately
    # If the node has two children:
        # Find the node's inorder successor (smallest node in right subtree)
        # Swap the value of the node and its inorder successor
        # Recursively remove the successor (which now has the current node's value)
    # Return the root of the updated tree


    if not root:
        return None

    if key < root.key:
        root.left = remove_bst(root.left, key)
    elif key > root.key:
        root.right = remove_bst(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        
        
        
    return root
        


"""
Example Input Tree #1: (tree depicted using keys) 

      10
     /  \
    /    \
   5      15
  / \     / \
 1   8   13  16


Input: root = 10, key = 10
Expected Output: 13
Expected Output Tree:

      13
     /  \
    /    \
   5      15
  / \       \
 1   8      16


Example Input Tree #2: (tree depicted using keys)

      10
     /  \
    /    \
   5      15
  / \     / \
 1   8   13  16
      \
       9 

Input: root = 10, key = 8
Expected Output: 10 (Should return a node object)
Expected Output Tree

      10
     /  \
    /    \
   5      15
  / \     / \
 1   9  13  16


Example Input Tree #3: (tree depicted using keys)

      10
     /  \
    /    \
   5      15
  / \     / \
 1   8   13  16
      \
       9 

Input: root = 10, key = 9
Expected Output: 10 (Should return a node object)
Expected Output Tree

      10
     /  \
    /    \
   5      15
  / \     / \
 1   8  13  16

"""