# brute force method
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle == "":
            return 0
        elif needle in haystack:
            return haystack.find(needle)
        else:
            return -1
            
# this is pretty much cheating



# a better solution
class Solution:
    def strStr(self, haystack:str, needle:str):
        if not needle:
            return 0
        retVal = -1
        for i in range(0,len(haystack)): # only required to loop through once
            if haystack[i:i + len(needle)] == needle:
                return i
        return retVal

# order of growth: O(n)
