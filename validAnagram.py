# Ashlyn Croft
# 2nd aug
# Checks for anagram
# Neet tutorial 2nd aug

class Solution:
    # Solution approach learned from NeetCode video tutorial
    # "Contains Duplicate" - accessed 2nd aug
    # https://neetcode.io/
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        return sorted(s) == sorted(t)