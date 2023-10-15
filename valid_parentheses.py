# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.


# my answer:

# class Solution:
#     def isValid(self, s: str) -> bool:
#         valid_parenth=[]
#         for char in s:
#             if(char=='{' or char=='[' or char=='('):
#                  valid_parenth.append(char)
#                  continue
#             else:
#                 if(len(valid_parenth)==0):
#                     return False

#                 if(char=='}'):
#                     if valid_parenth[len(valid_parenth)-1]=='{':
#                         valid_parenth.pop()
#                         continue
#                     else:
#                         return False
#                 if(char==']'):
#                     if valid_parenth[len(valid_parenth)-1]=='[':
#                         valid_parenth.pop()
#                         continue
#                     else:
#                         return False
#                 if(char==')'):
#                     if valid_parenth[len(valid_parenth)-1]=='(':
#                         valid_parenth.pop()
#                         continue
#                     else:
#                         return False
#         return len(valid_parenth)==0


# Answer I got from leetcode

# Since the last bracket that is opened must also be the first one to be closed, it makes sense to use a data structure that uses the Last In, First Out (LIFO) principle. Therefore, a stack is a good choice here.

# If a bracket is an opening bracet, we'll just push it on to the stack. If it's a closing bracket, then we'll use the pairs dictionary to check if it's the correct type of bracket (first pop the last opening bracket encountered, find the corresponding closing bracket, and compare it with the current bracket in the loop). If the wrong type of closing bracket is found, then we can exit early and return False.

# If we make it all the way to the end and all open brackets have been closed, then the stack should be empty. This is why we return len(stack) == 0 at the end. This will return True if the stack is empty, and False if it's not.

# class Solution(object):
#     def isValid(self, s):
#         stack = [] # only use append and pop
#         pairs = {
#             '(': ')',
#             '{': '}',
#             '[': ']'
#         }
#         for bracket in s:
#             if bracket in pairs:
#                 stack.append(bracket)
#             elif len(stack) == 0 or bracket != pairs[stack.pop()]:
#                 return False

#         return len(stack) == 0