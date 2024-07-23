# Session 1
# def is_subsequence(lst, sequence):
#   holder = []
#   for i in lst:
#     if i in sequence:
#       holder.append(i)

#   if holder == sequence:
#     return True
#   else: return False

# lst = [5, 1, 22, 25, 6, -1, 8, 10]
# sequence = [1, 6, -1, 11]
# print(is_subsequence(lst, sequence))

# def create_dictionary(keys, values):
#   dictionary = {}
#   for i in range(len(keys)):
#     dictionary[keys[i]] = values[i]
#   print(dictionary)

# keys = ["peanut", "dragon", "star", "pop", "space"]
# values = ["butter", "fly", "fish", "corn", "ship"]
# create_dictionary(keys, values)

# def print_pair(dictionary, target):
#   if dictionary is None:
#     return "not there"
#   if dictionary.get(target) is not None:
#     print("key: ", target)
#     print("value: ", dictionary.get(target))
#   else:
#     print("That pair does not exist!")

# dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
# print_pair(dictionary, "patrick")
# print_pair(dictionary, "plankton")
# print_pair(dictionary, "spongebob")

# def keys_v_values(dictionary):
#   sum_of_keys = sum(dictionary.keys())
#   sum_of_values = sum(dictionary.values())

#   if sum_of_keys > sum_of_values:
#     return "keys"
#   if sum_of_values > sum_of_keys:
#     return "values"
#   if sum_of_keys == sum_of_values:
#     return "balanced"

# dictionary1 = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
# greater_sum = keys_v_values(dictionary1)
# print(greater_sum)

# dictionary2 = {100:10, 200:20, 300:30, 400:40, 500:50, 600:60}
# greater_sum = keys_v_values(dictionary2)
# print(greater_sum)

# def restock_inventory(current_inventory, restock_list):
#   for items, quantity in restock_list.items():
#     if items in current_inventory:
#       current_inventory[items] += quantity
#     else:
#       current_inventory[items] = quantity

#   print(current_inventory)

# current_inventory = {
#   "apples": 30,
#   "bananas": 15,
#   "oranges": 10
# }

# restock_list = {
#   "oranges": 20,
#   "apples": 10,
#   "pears": 5
# }
# restock_inventory(current_inventory, restock_list)

# def calculate_gpa(report_card):
#   x = 0
#   for i in report_card.values():
#     if i == 'A':
#       x += 4
#     elif i == 'B':
#       x += 3
#     elif i == 'C':
#       x += 2
#     elif i == 'D':
#       x += 1
#     elif i == 'F':
#       x += 0
#   return round(x / len(report_card), 2)

# report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
# print(calculate_gpa(report_card))

# Session 2----------------------------------------------------------
# def cast_vote(votes, candidate):
#   if candidate in votes:
#     votes[candidate] += 1
#   else:
#     votes[candidate] = 1

# votes = {"Alice": 5, "Bob": 3}
# cast_vote(votes, "Alice")
# print(votes)
# cast_vote(votes, "Gina")
# print(votes)

# #def common_keys(dict1, dict2):
#   arr = []
#  # for key in dict1:
#     if key in dict2:
#       arr.append(key)
#   print(arr)

# dict1 = {"a": 1, "b": 2, "c": 3}
# dict2 = {"b": 4, "c": 5, "d": 6}
# common_list = common_keys(dict1, dict2)
# print(common_list)

# def get_highest_priority_task(tasks):

#   high_key = max(tasks, key=tasks.get)
#   tasks.pop(high_key)
#   return high_key

# tasks = {"task1": 8, "task2": 10, "task3": 9, "task4": 10, "task5": 7}
# perform_task = (get_highest_priority_task(tasks))
# print(perform_task)

# perform_task = (get_highest_priority_task(tasks))
# print(perform_task)

# perform_task = (get_highest_priority_task(tasks))
# print(perform_task)

# print(tasks)

# def count_occurrences(nums):
#   map = {}

#   for i in nums:
#     if i in map:
#       map[i] += 1

#     else:
#       map[i] = 1

#   return map

# nums = [1, 2, 2, 3, 3, 3, 4]
# print(count_occurrences(nums))

# def find_majority_element(elements):
#   map = {}
#   for i in elements:
#     if i in map:
#       map[i] += 1

#     else:
#       map[i] = 1

#   high_value = max(map.values())
#   for key, val in map.items():
#     if val == high_value and high_value > len(elements) / 2:
#         return key

# elements = [2, 2, 1, 1, 1, 2, 2]
# print(find_majority_element(elements))

# def hasDuplicates(nums, k):
#   map = {}
#   for i in range(len(nums)):
#     if nums[i] in map:
#       diff = i - map[nums[i]]
#       if diff <= k:
#         return True
#     map[nums[i]] = i
#   return False

# nums = [5, 6, 8, 2, 4, 6, 9]
# check1 = hasDuplicates(nums, 3)
# print(check1)
# check2 = hasDuplicates(nums, 4)
# print(check2)

# def hasDuplicates(nums, k):
#   recent_index = {}
#   for i in range(len(nums)):
#       if nums[i] in recent_index:
#           diff = i - recent_index[nums[i]]
#           if diff <= k:
#               return True
#       recent_index[val] = i
#   return False

# def peak_index_in_mountain_list(lst):
#   if len(lst) < 3:
#     print("not a mountain")

#   peak = 0
#   for i in range(len(lst)-1):
#     if lst[i] > lst[i + 1]:
#       peak = i
#   return peak

# mountain_lst = [0,3,8,0]
# peak = peak_index_in_mountain_list(mountain_lst)
# print(peak)

# def build_inventory(product_names, product_prices):
#   map = {}
#   for i in range(len(product_names)):
#     map[product_names[i]] = product_prices[i]
#   print(map)

# product_names = ["Apple", "Banana", "Orange"]
# product_prices = [0.99, 0.50, 0.75]

# build_inventory(product_names, product_prices)

# def update_or_warn(records, item, update_value):
#   for i in records:
#     if i == item:
#       records[i] = update_value
#       print(records)
#       return
#   print("not found")

# records = {"apple": 1, "banana": 2, "orange": 3}
# update_or_warn(records, "banana", 5)
# update_or_warn(records, "grape", 4)

# def attendance_rate(attendance_list):
#   present = 0
#   students = len(attendance_list)
#   for i in attendance_list:
#     if attendance_list[i] == "Present":
#       present += 1
#   return present / students * 100

# attendance_list = {
#   "Bluey": "Present",
#   "Bingo": "Absent",
#   "Snickers": "Absent",
#   "Winton": "Absent"
# }

# print(attendance_rate(attendance_list))

# def average_book_ratings(book_ratings):
#   map = {}
#   for i, j in book_ratings.items():
#     map[i] = round(sum(j) / len(j), 1)
#   print(map)

# book_ratings = {
#     "The Great Gatsby": [4.5, 3.0, 5.0],
#     "To Kill a Mockingbird": [4.8, 5.0, 4.0, 4.9]
# }

# average_book_ratings(book_ratings)

# def odd_keys_even_values(dictionary):
#   arr = []
#   for i in dictionary:
#     if i % 2 != 0 and dictionary[i] % 2 == 0:
#       arr.append(i)

#   return arr

# dictionary = {1: 2, 2: 6, 3: 5, 4: 4, 5: 8}
# final_list = odd_keys_even_values(dictionary)
# print(final_list)

# def team_with_best_average_score(games):
#   map = {}
#   for dict in games:
#     team = dict["team_name"]
#     score = dict["score"]

#     if team in map:
#       map[team]["total_score"] += score
#       map[team]["num_games"] += 1

#     else:
#       map[team] = {
#         "total_score" : score,
#         "num_games" : 1
#       }

#   best_team = None
#   best_score = 0

#   for i,j in map.items():
#     map[i] = j["total_score"] / j["num_games"]
#     if map[i] > best_score:
#       best_score = map[i]
#       best_team = i
#   return best_team

# games = [
#   {"team_name": "Lions",
#    "score": 23
#   },
#   {"team_name": "Tigers",
#    "score": 30
#   },
#   {"team_name": "Lions",
#    "score": 27
#   },
#   {"team_name": "Bears",
#    "score": 20
#   },
#   {"team_name": "Tigers",
#    "score": 24
#   },
#   {"team_name": "Bears",
#    "score": 22
#   }
# ]

# print(team_with_best_average_score(games))

# def find_unique_items(list_a, list_b):
#   map = {}

#   for i in list_a:
#     if i not in list_b:
#       map[i] = True

#   for i in list_b:
#     if i not in list_a:
#       map[i] = False
#   print(map)

# list_a = ["apple", "banana", "carrot"]
# list_b = ["apple", "banana", "date"]

# find_unique_items(list_a, list_b)

# def return_book(title, library):
#   if title in library:
#     library[title] += 1
#   else:
#     library[title] = 1
#   return library

# library = {"The Hobbit": 2, "1984": 1, "The Great Gatsby": 4}

# updated_lib = return_book("1984", library)
# print(updated_lib)

# updated_lib = return_book("The Giver", library)
# print(updated_lib)

# def dict_difference(d1, d2):
#   difference_dict = {}
#   for key in d1:
#     if key not in d2 or d1[key] != d2[key]:
#       difference_dict[key] = d1[key]

#   print(difference_dict)

# d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# d2 = {'b': 2, 'd': 1}

# dict_difference(d1, d2)

# def pop_stock(items, item_name, quantity):
#   if item_name not in items:
#     return "not in stock"

#   if quantity > items[item_name]:
#     return "not enough stock"
#   else:
#     items[item_name] -= quantity
#     if items[item_name] <= 0:
#       items.pop(item_name)
#     return items

# items = {"chocolate": 20, "candy": 5, "chips": 10}

# resultA = pop_stock(items, "candy", 2)
# resultB = pop_stock(items, "candy", 5)
# resultC = pop_stock(items, "lollipops", 5)
# resultD = pop_stock(items, "chocolate", 5)

# print(resultA)
# print(resultB)
# print(resultC)
# print(resultD)

# Unit 3 -----------------------------------------------
# def count_mississippi(limit):
#   for num in range(1, limit):
#     print( f"{num} mississippi")

# count_mississippi(6)

# def swap_ends(my_str):
#   start = my_str[0]
#   end = my_str[-1]
#   swapped_string = end + my_str[1:-1] + start
#   return swapped_string

# my_str = "boat"
# swapped = swap_ends(my_str)
# print(swapped)

# def is_pangram(my_str):
#   alphabet = set("abcdefghijklmnopqrstuvwxyz")

#   for char in my_str.lower():
#     if char in alphabet:
#       alphabet.remove(char)

#     if not alphabet:
#       return True

#   return False

# my_str = "The quick brown fox jumps over the lazy dog"
# print(is_pangram(my_str))

# str2 = "The dog jumped"
# print(is_pangram(str2))

# def reverse_string(my_str):
#   reverse = my_str[::-1]

#   return reverse

# my_str = "live"
# print(reverse_string(my_str))

# def first_unique_char(my_str):
#   map = {}
#   for char in my_str:
#     if char in map:
#       map[char] += 1
#     else:
#       map[char] = 1

#   for index, char in enumerate(my_str):
#     if map[char] == 1:
#       return index
#   return -1

# my_str = "leetcode"
# print(first_unique_char(my_str))

# str2 = "loveleetcode"
# print(first_unique_char(str2))

# str3 = "aabb"
# print(first_unique_char(str3))

# def min_distance(words, word1, word2):
#   index1 = None
#   index2 = None
#   min_dist = 0
#   for i in range(len(words)):
#     if words[i] == word1:
#       index1 = i
#     elif words[i] == word2:
#       index2 = i

#     if index1 is not None and index2 is not None:
#       min_dist = abs(index1 - index2)
#   return min_dist

# words = ["the", "quick", "brown", "fox", "jumped", "the"]
# dist1 = min_distance(words, "quick", "jumped")
# dist2 = min_distance(words, "the", "jumped")
# print(dist1)
# print(dist2)

# words2 = ["code", "path", "code", "contribute", "practice"]
# dist3 = min_distance(words2, "code", "practice")
# print(dist3)

# def wordPattern(pattern, s):
#   words = s.split()

#   if len(pattern) != len(words):
#       return False

#   pattern_to_word = {}
#   word_to_pattern = {}

#   for char, word in zip(pattern, words):
#       if char in pattern_to_word:
#           if pattern_to_word[char] != word:
#               return False
#       else:
#           pattern_to_word[char] = word

#       if word in word_to_pattern:
#           if word_to_pattern[word] != char:
#               return False
#       else:
#           word_to_pattern[word] = char

#   return True

# pattern = "abba"
# s = "dog cat cat dog"
# print(wordPattern(pattern, s))
# s2 = "dog cat cat fish"
# print(wordPattern(pattern, s2))

# pattern2 = "aaaa"
# s3 = "dog cat dog cat"
# print(wordPattern(pattern2, s3))
# s4 = "dog dog dog dog"
# print(wordPattern(pattern2, s4))

# def compress_string(my_str):
#     compressed = ''
#     counter = 0
#     for char in range(len(my_str)): #to check the last pair
#         if char == len(my_str)-1:
#             compressed += my_str[char]
#             compressed += str(counter + 1)

#         elif my_str[char] == my_str[char + 1]:
#             counter += 1

#         else:
#             compressed += my_str[char]
#             compressed += str(counter + 1)
#             counter = 0

#     return compressed if len(compressed) < len(my_str) else my_str

# my_str = "aaaaabbcccd"
# compressed_Str = compress_string(my_str)
# print(compressed_Str)

# my_str2 = "abcde"
# compressed_Str2 = compress_string(my_str2)
# print(compressed_Str2)

# def reverse_only_letters(s):
#     arr = list(s)
#     result = []
#     end = len(arr) - 1
#     start = 0

#     while end > -1:
#         if arr[start].isalpha() and arr[end].isalpha():
#             result.append(arr[end])
#             end -= 1
#             start += 1

#         elif arr[start].isalpha() is False:
#             result.append(arr[start])
#             start += 1

#         elif arr[end].isalpha() is False:
#             end -= 1

#     return "".join(result)

# s = "a-bC-dEf-ghIj"
# reversed_s = reverse_only_letters(s)
# print(reversed_s)

# def longest_uniform_substring(s):
#     count = 1
#     max = 1
#     arr = list(s)
#     for i in range(len(arr) - 1):

#         if arr[i] == arr[i + 1]:
#             count += 1

#         elif count > max:
#             max = count
#             count = 1

#     if count > max:
#         max = count

#     return max

# s1 = "aabbbbCdAA"
# l1 = longest_uniform_substring(s1)
# print(l1)

# s2 = "abcdef"
# l2 = longest_uniform_substring(s2)
# print(l2)

# Unit 4 -----------------------------------------------
# def remove_duplicates(nums):
#   if nums is None:
#     return 0

#   j = 1
#   for i in range(1, len(nums)):
#     if nums[i] != nums[i-1]:
#       nums[j] = nums[i]
#       j += 1
#   return j
#   # nums = set(nums)
#   # return len(nums)

# nums = [1,1,2,3,4,4,4,5]
# print(nums)
# print(remove_duplicates(nums))
# print(nums) # same list

# [1,1,2,3,4,4,4,5]
# 5
# [1,2,3,4,5]

# def is_long_pressed(name, typed):
#   i = 0
#   j = 0

#   while j < len(typed):
#     if i < len(name) and name[i] == typed[j]:
#       j += 1
#       i += 1

#     elif typed[j] == typed[j-1]:
#       j += 1

#     else:
#         return False
#   return True

# Unit 5 -----------------------------------------------

# class Pokemon:
#   def __init__(self, name, types, evolution):
#       self.name = name
#       self.types = types
#       self.is_caught = False
#       self.evolution = evolution

#   def print_pokemon(self):
#       print({
#           "name": self.name,   # Output: "name": "Squirtle",
#           "types": self.types, # Output: "types": ["Water"],
#           "is_caught": self.is_caught # Output: "is_caught": False
#       })

#   def catch(self):
#       self.is_caught = True

#   def choose(self):
#       if self.is_caught is True:
#           print(self.name + " I choose you!")
#       else:
#           print(self.name + " is wild! Catch them if you can!")

#   def add_type(self, new_type):
#       self.types.append(new_type)

# def get_by_type(my_pokemon, pokemon_type):
#   arr = []
#   for i in my_pokemon:
#       if pokemon_type in i.types:
#           arr.append(i.name)

#   return arr

# def get_evolutionary_line(starter_pokemon):
#   arr = []
#   if starter_pokemon.evolution is None:
#       arr.append(starter_pokemon.name)
#       return arr
#   else:
#       arr.append(starter_pokemon.name)
#       while starter_pokemon.evolution is not None:
#           starter_pokemon = starter_pokemon.evolution
#           arr.append(starter_pokemon.name)
#       return arr

# charizard = Pokemon("Charizard", ["fire", "flying"], None)
# charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
# charmander = Pokemon("Charmander", ["fire"], charmeleon)

# charmander_list = get_evolutionary_line(charmander)
# print(charmander_list)

# charmeleon_list = get_evolutionary_line(charmeleon)
# print(charmeleon_list)

# charizard_list = get_evolutionary_line(charizard)
# print(charizard_list)

# class Node:

#   def __init__(self, value, next=None):
#     self.value = value
#     self.next = next

# def print_linked_list(head):
#   arr = []
#   current = head
#   arr.append(current.value)
#   while current.next is not None:
#     arr.append(" -> ")
#     arr.append(current.next.value)
#     current = current.next
#   s = ""
#   for i in arr:
#     s += i
#   print(s)

# node1 = Node("a")
# node2 = Node("b")
# node3 = Node("c")
# node4 = Node("d")
# node5 = Node("e")

# node1.next = node2
# node2.next = node3
# node3.next = node4
# node4.next = node5

# print_linked_list(node1)

# Session 2

# class Card():
#   def  __init__(self, suit, rank):
#     self.suit = suit
#     self.rank = rank

# def is_two_pair(player_hand):
#   memo = {}

#   for card in player_hand:
#     if card.rank in memo:
#       memo[card.rank] += 1
#     else:
#       memo[card.rank] = 1

#   pairs = 0
#   for count in memo.values():
#     if count == 2:
#       pairs += 1

#   return pairs == 2

# card_one = Card("Hearts", "Ace")
# card_two = Card("Hearts", "4")
# card_three = Card("Diamonds", "Ace")
# card_four = Card("Diamonds", "4")
# card_five = Card("Diamonds", "6")
# card_six = Card("Diamonds", "7")

# player_one_hand = [card_one, card_two, card_three, card_four, card_five]
# print(is_two_pair(player_one_hand))

# player_two_hand = [card_two, card_three, card_four, card_five, card_six]
# print(is_two_pair(player_two_hand))

# class Node:
#   def __init__(self, value, next=None):
#     self.value = value
#     self.next = next

# node_1 = Node("Barbie")
# node_2 = Node("President Barbie")
# node_3 = Node("Weird Barbie")
# node_4 = Node("Ken")

# node_1.next = node_2
# node_2.next = node_3
# node_3.next = node_4

# print(node_1.value, "->", node_1.next.value)
# print(node_2.value, "->", node_2.next.value)
# print(node_3.value, "->", node_3.next.value)
# print(node_4.value, "->", node_4.next)

# class Card():
#   def  __init__(self, suit, rank, next = None):
#     self.suit = suit
#     self.rank = rank
#     self.next = next

#   def print_card(self):
#     print(self.suit, self.rank)

#   def is_valid(self):
#     suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
#     ranks = ["2", "3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
#     return self.suit in suits and self.rank in ranks

#   def get_value(self):
#     ranks = ["2", "3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]
#     if self.is_valid():
#       for character in ranks:
#         if character == self.rank:
#           if character == "Ace":
#             return 1
#           elif character == "Jack":
#             return 11
#           elif character == "Queen":
#             return 12
#           elif character == "King":
#             return 13
#           else:
#             return int(self.rank)

# class Hand:
#   def __init__(self):
#       self.cards = []

#   def add_card(self, card):
#     self.cards.append(card)

#   def remove_card(self, card):
#     self.cards.remove(card)

#   def print_hand(self):
#     for card in self.cards:
#       card.print_card()

# def sum_hand(hand):
#   sum = 0
#   for card in hand.cards:
#     sum += card.get_value()
#   return sum

# def print_hand(starting_card):
#   result = []
#   current = starting_card
#   result.append(starting_card)
#   while current is not None:
#     current = current.next
#     result.append(current)
#   return result

# card = Card("Hearts", "5")
# card.print_card()
# print(card.is_valid())
# print(card.get_value())
# card_one = Card("Hearts", "3")
# card_two = Card("Spades", "8")

# player1_hand = Hand()
# # cards = []

# player1_hand.add_card(card_one)
# # cards = [card_one]
# player1_hand.print_hand()
# print("\n")

# player1_hand.add_card(card_two)
# # cards = [card_one, card_two]
# player1_hand.print_hand()
# print("\n")

# player1_hand.remove_card(card_one)
# # cards = [card_two]
# player1_hand.print_hand()
# print("\n")

# card_one = Card("Hearts", "3")
# card_two = Card("Hearts", "Jack")
# card_three = Card("Spades", "3")

# hand = Hand()
# hand.add_card(card_one)
# hand.add_card(card_two)
# hand.add_card(card_three)

# sum = sum_hand(hand)
# print(sum)
# card_one = Card("Hearts", "3")
# card_two = Card("Hearts", "4")
# card_three = Card("Diamonds", "King")

# card_one.next = card_two
# card_two.next = card_three

# print_hand(card_one)
# class Node:
#   def __init__(self, value, next=None):
#     self.value = value
#     self.next = next

# example = Node(3, Node(1, Node(2, Node(1))))

# # Helper function to print the linked list
# def print_list(node):
#   current = node
#   while current:
#       print(current.value, end=" -> " if current.next else "")
#       current = current.next
#   print()

# # I have a bug!
# def remove_tail(head):
#   if head is None: # If the list is empty, return None
#       return None
#   if head.next is None: # If there's only one node, removing it leaves the list empty
#       return None
#   # Start from the head and find the second-to-last node
#   current = head
#   #while current.next:
#   #  current = current.next
#   #  print(current.value)
#   #current = None
#   #return head
#   while current.next.next:

#     current = current.next
#   current.next = None
#   return head

# #print_list(example)

# print_list(remove_tail(example))


# Unit 6
# class Node:

#   def __init__(self, value, next=None):
#     self.value = value
#     self.next = next


# def print_list(node):
#   current = node
#   while current:
#     print(current.value, end=" -> " if current.next else "")
#     current = current.next
#     if current == node:
#       print(current.value)
#       break
#   print()


# def make_circular(head):
#   current = head
#   while current:
#     if current.next is None:
#       current.next = head
#       return
#     current = current.next

# def add_two_numbers(head_a, head_b):
#   currA = head_a
#   currB = head_b
#   s1 = ""
#   s2 = ""
#   while currA:
#     s1 += currA.value
#     currA = currA.next
#   while currB:
#     s2 += currB.value
#     currB = currB.next
#   s1[::-1]
#   s2[::-1]
#   return int(s1) + int(s2)

# n1 = Node("2")
# n2 = Node("4")
# n3 = Node("3")

# n1.next = n2
# n2.next = n3

# m1 = Node("5")
# m2 = Node("6")
# m3 = Node("4")

# m1.next = m2
# m2.next = m3

# print_list(n1)
# print_list(m1)
# print(add_two_numbers(n1, m1))

# Unit 7
# def factorial(n):
#   if n == 0:
#     return 1
#   if n == 1:
#     return 1
#   return n * factorial(n-1)
  
# print(factorial(5))

# def sum_list(lst):
#   if not lst:
#     return 0
#   return lst[0] + sum_list(lst[1:])

# lst = [1,2,3,4,5]
# print(sum_list(lst))

# def is_power_of_two(n):
#   if n == 1:
#     return True
#   elif n % 2 != 0:
#     return False

#   return is_power_of_two(n//2)

# print(is_power_of_two(16))

# def find_floor(lst, x):
#   for i in range(len(lst)):
#     if lst[i] >= x:
#       return i-1


# lst = [1, 2,6]
# x = 5
# print(find_floor(lst, x))

# def repeat_hello(n):
#   if n > 0:
#     print("Hello")
#     repeat_hello(n - 1)

# repeat_hello(5)

# def iterative_repeat_hello(x):
#   for num in range(x):
#     print("Hello")

# iterative_repeat_hello(5)


# def factorial(n):
#   if n <= 1:
#     return 1
#   return n * factorial(n-1)

# def sum_list(lst):
#   if not lst:
#     return 0
#   # if len(lst) == 0:
#   #   return 0
#   return lst[0] + sum_list(lst[1:])

# print(sum_list([1,2,3,4,5]))

# def is_power_of_two(n):
#   if n == 1:
#     return True
#   elif n % 2 != 0:
#     return False
#   return is_power_of_two(n//2)

# print(is_power_of_two(6))

# def binary_search(lst, target):
#   left = 0
#   right = len(lst) - 1

#   while left <= right:
#     mid =  left + (right - left) // 2
#     if lst[mid] == target:
#       return mid
#     elif lst[mid] < target:
#       left = mid + 1
#     else: 
#       right = mid - 1
#   return -1


# lst = [1, 3, 5, 7, 9, 11, 13, 15]
# target = 11
# print(binary_search(lst, target))

# def rec_binary_search(lst, target, left, right):
#   if left <= right:
#     mid =  left + (right - left) // 2
#   #base
#     if lst[mid] == target:
#       return mid
#   #recursive
#     elif lst[mid] < target:
#       return rec_binary_search(lst, target, mid + 1, right)
#     else:
#       return rec_binary_search(lst, target, left, mid - 1)
#   else:
#     return -1

# lst = [1, 3, 5, 7, 9, 11, 13, 15]
# left = 0
# right = 7
# target = 11
# print(rec_binary_search(lst, target, left, right))


# def find_last(lst, target):
#     left = 0
#     right = len(lst) - 1
#     last = -1

#     while left <= right:
#       mid =  left + (right - left) // 2
#       if lst[mid] == target:
#         # while lst[mid] == target:
#         #   mid += 1
#         # return mid-1
#         last = mid
#         left = mid + 1  # Continue searching in the right half
#       elif lst[mid] < target:
#         left = mid + 1
#       else: 
#         right = mid - 1
#     return last

# lst = [1, 3, 5, 7, 11, 11, 11, 11, 15]
# target = 11
# print(find_last(lst, target))


# def find_last(lst, target):
#   left, right = 0, len(lst) - 1
#   last_occurrence = -1

#   while left <= right:
#       mid = (left + right) // 2

#       if lst[mid] == target:
#           last_occurrence = mid
#           left = mid + 1  # Continue searching in the right half
#       elif lst[mid] < target:
#           left = mid + 1
#       else:
#           right = mid - 1

#   return last_occurrence

# lst = [1, 3, 5, 7, 9, 11, 11, 13, 15]
# target = 11
# print(find_last(lst, target))


def find_floor(lst, x):
  max = 0
  for i in range(len(lst)):
    if lst[i] > max and lst[i] < x:
      max = i
  return max

lst = [1, 2, 8, 10, 11, 12, 19]
x = 5
print(find_floor(lst, x))


def find_floor(arr, x):
  low, high = 0, len(arr) - 1
  floor_value = None  # Initialize to None to handle the case where all elements are greater than x

  while low <= high:
      mid = (low + high) // 2

      if arr[mid] <= x:
          floor_value = arr[mid]  # arr[mid] could be a potential floor
          low = mid + 1  # Look for a larger element that might also be a floor
      else:
          high = mid - 1  # Search in the left half

  return floor_value