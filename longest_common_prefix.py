# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

# solution

# class Solution:
# my-solution
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         minimum=min(strs,key=len)
#         common_prefix=""
#         for i in range(len(minimum)):
#             char=strs[0][i]
#             if(all(s[i]==char for s in strs)):
#                 common_prefix+=char
#             else:
#                 break
#         return common_prefix

# Solution i got

# class Solution:
#     def longestCommonPrefix(self, v: List[str]) -> str:
#         ans=""
#         v=sorted(v)
#         first=v[0]
#         last=v[-1]
#         for i in range(min(len(first),len(last))):
#             if(first[i]!=last[i]):
#                 return ans
#             ans+=first[i]
#         return ans