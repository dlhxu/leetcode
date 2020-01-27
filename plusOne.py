class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        # turn into int
        intSoFar = 0
        i = len(digits) - 1
        power = 0
        while (i>=0):
            intSoFar += (digits[i] * (10**power))
            i-=1
            power+=1
        
        # plus one
        newInt = intSoFar + 1
        
        # find number of digits
        temp = newInt
        newPower = 0
        while (temp > 0):
            temp //= 10
            newPower +=1
        
        # turn back into an array
        newDigits = [None]*newPower
        i = newPower - 1
        while(i>=0):
            newDigits[i] = newInt % 10
            newInt //= 10
            i-=1
            
        return newDigits
