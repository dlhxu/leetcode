class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        containsDuplicate = False
        i = 0
        seen = {}
        while (i < len(nums) and not containsDuplicate):
            if(seen.get(nums[i])):
                containsDuplicate = True
            else:
                seen[nums[i]] = 1
            i+=1
        return containsDuplicate
