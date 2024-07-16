'''Unit 6 Session 1: Working with Linked Lists'''

'''Problem 1'''

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

head = Node(4, Node(3, Node(2)))


'''Problem 2'''

def count_element(head, val):
    ans = 0  
    temp_head = head
    while temp_head:
        if temp_head.value == val:
            ans += 1
        temp_head = temp_head.next
    return ans  

lst = Node(3, Node(1, Node(2, Node(1))))
# print(count_element(lst, 1))


'''Problem 3'''

# Helper function to print the linked list
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()


# I have a bug! 
def remove_tail(head):
    if head is None: # If the list is empty, return None
        return None
    if head.next is None: # If there's only one node, removing it leaves the list empty
        return None 

  # Start from the head and find the second-to-last node
    current = head
    while current.next and current.next.next: 
        current = current.next

    current.next = None # Remove the last node by setting second-to-last node to None
    return head


# Test cases
# head = Node(1, Node(2, Node(3, Node(4))))
# print("Original List")
# print_list(head)   

# head = remove_tail(head)

# print("After removing tail:")
# print_list(head)

'''Problem 4'''
# class Node:
#    def __init__(self, value, next=None):
#        self.value = value
#        self.next = next

def find_middle_element(head):
    # length = find_length(head)
    slow_pointer  = head
    fast_pointer = head
    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
    return slow_pointer.value
    
head = Node(1, Node(2, Node(3, Node(4))))
# print(find_middle_element(head))


'''Problem 5'''
# class Node:
#    def __init__(self, value, next=None):
#        self.value = value
#        self.next = next

def is_palindrome(head):
    lst = []

    curr = head
    while curr:
        lst.append(curr.value)
        curr = curr.next

    left = 0
    right = len(lst) - 1
    while left < right:
        if lst[left] != lst[right]:
            return False
        left += 1
        right -= 1
    return True
    # left_pointer = head
    # right_pointer = tail
    
    # while left_pointer != right_pointer or left_pointer.next != right_pointer:
    #     if left_pointer != right_pointer:
    #         return False
    #     left_pointer = left_pointer.next

    class Node:
        def __init__(self, value=None, next=None):
            self.value = value
            self.next = next

    def is_palindrome(head):
        if head is None or head.next is None:
            return True  # A list with 0 or 1 element is a palindrome

        # Find the middle of the list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half of the list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        # Compare the first half and the reversed second half
        left, right = head, prev
        while right:  # Only need to compare till the end of the second half
            if left.value != right.value:
                return False
            left = left.next
            right = right.next

        return True

'''Problem 6'''

def reverse(head):
    previous = None
    current = head

    while current:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node
    return previous

print_list(reverse(Node(1, Node(2, Node(3)))))
