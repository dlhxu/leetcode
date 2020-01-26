class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # create a map to store the values that have already been seen as keys, with value equal to the index they were seen at
        seenVals = {}
        twoSum = []
        for i in range(len(nums)):
            
            # at every step, we're looking to see if the number that will sum with current num to reach the target has actually been seen before, if so we immediately return
            complement = target - nums[i]
            if (complement in seenVals):
                twoSum.append(seenVals[complement])
                twoSum.append(i)
                return twoSum
            
            # otherwise we record that we have seen a value, and its index
            else:
                seenVals[nums[i]] = i
