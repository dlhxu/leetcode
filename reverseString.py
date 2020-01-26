class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        
        # what we want to do is "reflect" the characters across the midline
        # to do this, we swap the value at index i with the value i indices to the right of the end, which effectively swaps a character with its counterpart across the midline
        # we repeat this action by iterating through the array, and at the middle, we stop because all characters have been swapped at this point
        # we make this possible by using two pointers, one for each end of the array
        # both of these pointers increment towards the midline, and iteration stops when they reach the same point, or cross paths because we know that at that point all characters have been swapped
        
        left = 0
        right = len(s) - 1
        
        while (left < right):
            temp = s[right]
            s[right] = s[left]
            s[left] = temp
            left +=1
            right -=1
