#Problem 1: Long Pressed

# def is_long_pressed(name, typed):
#   name_pointer = 0
#   typed_pointer = 0

#   while name_pointer < len(name) and typed_pointer < len(typed):
#     if name[name_pointer] == typed[typed_pointer]:
#       name_pointer += 1
#       typed_pointer += 1
#     elif typed[typed_pointer] == typed[typed_pointer - 1]:
#       typed_pointer += 1
#     else:
#       return False

#   if name_pointer == len(name):
#     return True

# #           .
# name = "aleex"
# #             .
# typed = "aaleex"
# print(is_long_pressed(name, typed))

# name2 = "saeed"
# typed2 = "ssaaedd"
# print(is_long_pressed(name2, typed2))

# name3 = "courtney"
# typed3 ="courtney"
# print(is_long_pressed(name3, typed3))


#Problem 2: Sharing Cookies
# def find_content_children(s, g):
#   s.sort()
#   g.sort()

#   child = 0
#   cookie = 0
#   # counter = 0

#   while cookie < len(s) and child < len(g):
#     if g[child] <= s[cookie]:
#       child += 1
#     cookie += 1
#   return child


# g = [1, 2, 3]
# s = [1, 1, 3]
# print(find_content_children(s, g))
# # Output: 2

# g = [1, 1]
# s = [2, 2, 2]
# print(find_content_children(s, g))
# Output: 2

#[1,3,5] =g 
#[1,2,3]=s
# OUT PUT?? 2
#  : 

#Some explaination, think of len(g) as total number of children, each index i representing the child number and each s[i] representing the chocolate chips that the child wants on cookie (atleast)
# len(s) represent total number of cookies and each s[j] contain number of chocolate chips on j, maximize the number of children having atleast their desired number of cookie.

# Problem 3: Valid Palindrome

def is_plaindrome(s, left, right):
  # return s == s[::-1]
  while left < right:
    if s[left] != s[right]:
      return False
    left += 1
    right -= 1
  return True
  # so this method basically checks if it actually is a plaindrome, whereas the main method just handles if any of the characters in the plaindrome is mismatched or invalidates it

  
def valid_palindrome(s):
  left = 0
  right = len(s) -1

  while left < right:
    if s[left] == s[right]:
      left +=1
      right -=1
    else:
      # i think we need to use the helper method here
      return is_plaindrome(s, left + 1, right) or is_plaindrome(s, left, right - 1)
  return True
  

s = "aba"
s2 = "abca"
s3 = "abc"

print(valid_palindrome(s))
print(valid_palindrome(s2))
print(valid_palindrome(s3))