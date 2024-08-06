# # Problem 1:
# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#       self.val = val
#       self.left = left
#       self.right = right

# def is_mirror(left, right):
#   if not left and not right:
#     return True
#   if not left or not right:
#     return False
#   if left.val != right.val:
#     return False
#   return is_mirror(left.left, right.right) and is_mirror(left.right, right.left)

# def is_symmetric(root):
#   if not root:
#     return True
#   return is_mirror(root.left, root.right)


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(2)
# # root.left.left = TreeNode(3)
# root.right.right = TreeNode(3)
# root.left.right = TreeNode(3)
# # root.right.left = TreeNode(4)
# print(is_symmetric(root))

"""
Example Tree #1:

       1
     /   \
    /     \
   2       2 left = 2, right = 2
  / \     / \
 3   4   4   3
           |


Input: root = 1
Expected Output: True


Example Tree #2:

        1
      /   \
     /     \
    2       2
     \       \
      3       3


Input: root = 1
Expected Output: False
"""

# Problem 2
# root.left and root.right separatly
# return a list of paths
# path is from root to leaft (no child)

# class TreeNode:
#   def __init__(self, val=0, left=None, right=None):
#       self.val = val
#       self.left = left
#       self.right = right

# def binary_tree_paths(root):
#   paths = []
  
#   # if not root:
#   #   return None

#   helper(root, "", paths)
#   return paths
  
# def helper(node, path, paths):
#   if not node:
#     return None

#   if path:
#     path += "->" + str(node.val)
#   else:
#     path = str(node.val)
  
#   if not node.left and not node.right:
#     paths.append(path)
#   else:
#     helper(node.left, path, paths)
#     helper(node.right, path, paths)


# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.right = TreeNode(5)
# print(binary_tree_paths(root))
  

"""
Example Input Tree #1:

  1
 / \
2   3
 \  
  5         

Example Input: root = 1
Expected Output: ["1->2->5", "1->3"]
["1->3", "1->2->5"] is also valid

Example Input Tree #2:

  1    

Example Input: root = 1
Expected Output: ["1"]
"""


# Problem 3
class TreeNode:
  def __init__(self, val=0, left=None, right=None):
      self.val = val
      self.left = left
      self.right = right

def in_order_traversal(root, nodes):
  if root is not None:
    in_order_traversal(root.left, nodes)
    nodes.append(root.val)
    in_order_traversal(root.right, nodes)
    

def min_diff_in_bst(root):
  nodes = []
  in_order_traversal(root, nodes)

  min_diff = float('inf')

  for i in range(1, len(nodes)):
    min_diff = min(min_diff, nodes[i] - nodes[i - 1])

  return min_diff


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
print(min_diff_in_bst(root))

#it works


"""
Example Input Tree #1:

    4
   / \
  2   6
 / \  
1   3
      4

      # 4 - 2 < 3 - 2

Example Input: root = 4
Expected Output: 1 
Explanation: The smallest difference between any two nodes is 1 (2 - 1 = 1, 3 - 2 = 1)

Example Input Tree  #2: 

   1
  / \
 0  48
    / \  
   12 49

Example Input: root = 1
Expected Output: 1 
Explanation: The smallest difference between any two nodes is 1 (1 - 0 = 1)
"""