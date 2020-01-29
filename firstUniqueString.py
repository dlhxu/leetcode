class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        occurrences = {}
        
        # determine number of occurrences of each character
        for char in s:
            if (char in occurrences):
                occurrences[char] +=1
            else:
                occurrences[char] = 1
        
        # determine if a character is unique
        for i in range (len(s)):
            if (occurrences[s[i]] == 1):
                return i
        
        return -1
