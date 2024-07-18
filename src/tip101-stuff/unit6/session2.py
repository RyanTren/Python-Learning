# #Problem 1
# class Node:
#   def __init__(self, value, next=None):
#       self.value = value
#       self.next = next

# def is_circular(head):
#   if not head:
#     return False
#   current = head
#   while current.next:
#     current = current.next
#     if current.next == head:
#       return True
#   return False
    
# # Example Usage:
# node3 = Node(3)
# node2 = Node(2, node3)
# node1 = Node(1, node2)
# node3.next = node1

# # num1 -> num2 -> num3 -> num1
# print(is_circular(node1))

# # var1 -> var2 -> var3
# head = Node("var1", Node("var2", Node("var3")))
# print(is_circular(head))


# Example Output:
# True
# False


# class Node:
#   def __init__(self, value, next=None):
#       self.value = value
#       self.next = next

# def find_last_node_in_cycle(head):
#   if not head or not head.next:
#       return None

#   slow = fast = head
#   has_cycle = False

#   # Phase 1: Detecting the cycle using the Floyd's Cycle Detection Algorithm
#   while fast and fast.next:
#       slow = slow.next
#       fast = fast.next.next
#       if slow == fast:
#           has_cycle = True
#           break

#   # If there's no cycle, return None
#   if not has_cycle:
#       return None

#   # Phase 2: Identifying the start of the cycle
#   slow = head
#   while slow != fast:
#       slow = slow.next
#       fast = fast.next

#   # Find the last node in the cycle
#   cycle_start = slow
#   last_node = cycle_start
#   while last_node.next != cycle_start:
#       last_node = last_node.next

#   return last_node.value

# node4 = Node(4)
# node3 = Node(3, node4)
# node2 = Node(2, node3)
# node1 = Node(1, node2)
# node4.next = node2

# print(find_last_node_in_cycle(node1))
  
# What is the multiple pass technique?
# I'm about to board soon, is it good if I leave early

#problem 3
class Node:
  def __init__(self, value, next=None):
      self.value = value
      self.next = next

def partition(head, val):
  # Create two temp heads to start the less and greater lists
  less_head = Node(0)
  greater_head = Node(0)

  # These pointers will be used to add nodes to the less and greater lists
  less = less_head
  greater = greater_head

  # Traverse the original list
  current = head
  while current:
      if current.val < val:
          less.next = current
          less = less.next
      else:
          greater.next = current
          greater = greater.next

      current = current.next

  # Important: end the greater list to prevent cycles
  greater.next = None

  # Attach the end of the less list to the start of the greater list
  # Important: Skip the temp head
  less.next = greater_head.next

  return less_head.next



