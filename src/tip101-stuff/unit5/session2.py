class Pokemon():
	def  __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp # hit points
		self.damage = damage # The amount of damage this pokemon does to its opponent every attack
		
	
	def attack(self, opponent):
		opponent.hp -= self.damage
		if opponent.hp <= 0:
			opponent.hp = 0
			print(f"{opponent.name} fainted")
		else:
			print(f"{self.name} dealt {self.damage} damage to {opponent.name}")
		

# jigglypuff = Node("Jigglypuff")
# wigglytuff = Node("Wigglytuff")
# jigglypuff.next = wigglytuff

def add_first(head, new_node):
  new_node.next = head
  return new_node 

def get_tail(head):
  if not head:
    return None
  current = head
  while current.next:
    current = current.next
  return current.value


def ll_replace(head, original, replacement):
  current = head
  while current:
    if current.value == original:
      current.value = replacement
    current = current.next


def listify_first_n(head, n):
    # List to store the values of nodes
    values = []
    # Start from the head node
    current = head
    # Counter to track the number of nodes processed
    count = 0
    # Loop until 'current' is not None and 'count' is less than 'n'
    while current is not None and count < n:
        # Append current node's value to the list
        values.append(current.value)
        # Move to the next node
        current = current.next
        # Increment the counter
        count += 1
    # Return the list of collected values
    return values



# def ll_insert(head, val, i):
#     # Handle the case where the list is initially empty or `i` is 0
#     if not head or i == 0:
#         # return Node(val, head)

#     # Traverse to find the insertion point
#     # current = head
#     # count = 1  # Start count at 1 since we've already handled `i == 0`
#     # while current:
#         # Insert at index `i` by adjusting the `next` pointers
#         if count == i:
#             # new_node = Node(val, current.next)
#             # current.next = new_node
#             return head
#         current = current.next
#         count += 1

#     # If `i` was beyond the end, append to the last
#     if count < i:
#         # current.next = Node(val)

#     # return head


# def list_to_linked_list(lst):
#     if not lst:  # Check if the array is empty
#         return None
#     head = Node(lst[0])  # Create the head node with the first element
#     current = head
#     for value in lst[1:]:  # Iterate over the rest of the elements
#         current.next = Node(value)  # Create a new node and link it
#         current = current.next
#     return head

# poliwag = Node("Poliwag")
# poliwhirl = Node("Poliwhirl")
# poliwrath = Node("Poliwrath")

# poliwag.next = poliwhirl
# poliwhirl.next = poliwrath

# poliwrath.prev = poliwhirl
# poliwhirl.prev = poliwag

def print_reverse(tail):
    values = []
    current = tail
    while current:
        values.append(str(current.value))
        current = current.prev
    print(" ".join(values))