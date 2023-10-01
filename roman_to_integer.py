# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

 

# Example 1:

# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:

# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:

# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

# Constraints:

# 1 <= s.length <= 15
# s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
# It is guaranteed that s is a valid roman numeral in the range [1, 3999]

# -----------------------------------------------------------------------

# solution

# my-solution

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         my_Tuple=[('I',1),('V',5),('X',10),('L',50),('C',100),('D',500),('M',1000)]
        
#         # To find the corresponding interger value 
#         def find_value(string):
#             for x in my_Tuple :
#                 if(string == x[0]):
#                     return x[1]  

#         # check whether subtraction is required or not
#         def check_subtract(str1, str2):
#             if str1=="I" and (str2=='V' or str2=='X'):
#                 return True
#             elif str1=='X' and (str2=='L' or str2=='C'):
#                 return True
#             elif str1=='C' and (str2=='D' or str2=='M'):
#                 return True
#             else:
#                 return False



#         # To calculate the total value

#         num=0
#         skip=False;

#         for idx, value in enumerate(s):
#             if(skip==True):
#                 skip=False
#                 continue
                
#             # If it's a last element no need to check
#             if( idx is not len(s)-1):
#                 subract=check_subtract(value,s[idx+1])
             
#                 if(subract):
#                     skip=True
#                     value1=find_value(s[idx+1])-find_value(value)
#                     num=num+value1;

#                 else:
#                     skip=False
#                     num_value=find_value(value)  
#                     num=num+num_value
#             else:
#                 skip=False
#                 num_value=find_value(value)
#                 num=num+num_value
 
#         return num;      
    
# solution I gotclass Solution:
    # def romanToInt(self, s: str) -> int:
    #     m = {
    #         'I': 1,
    #         'V': 5,
    #         'X': 10,
    #         'L': 50,
    #         'C': 100,
    #         'D': 500,
    #         'M': 1000
    #     }
        
    #     ans = 0
        
    #     for i in range(len(s)):
    #         if i < len(s) - 1 and m[s[i]] < m[s[i+1]]:
    #             ans -= m[s[i]]
    #         else:
    #             ans += m[s[i]]
        
    #     return ans