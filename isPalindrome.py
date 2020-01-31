class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        left = 0
        right = len(s) - 1
        s = s.lower()
        
        while(left < right):
            
            # check that left and right are both alphanumerics
            if (s[left].isalnum() and s[right].isalnum()):
                if (s[left] != s[right]):
                    return False
                else:
                    left += 1
                    right -= 1
            else:
                if (not s[left].isalnum()):
                    left += 1
                if (not s[right].isalnum()):
                    right -= 1
        
        return True
