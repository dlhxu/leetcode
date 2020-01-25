class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # initialize problem by setting globalmax to default val of the first index
        maxSum = nums[0]
        
        # variable maxSumSoFar tracks the max subarray seen up until this point
        maxSumSoFar = nums[0]
        
        # examine the maxSum in the array after index 0
        
        # the essence of this problem is to determine the best subarray sum at this point in time, comparing the value at i vs the best subarray sum prior to this point
        
        # By choosing the best between the current value at i, and the previous best value, it is guaranteed that the next iteration will again be comparing the best subarray prior to that point in the array and the current value
        
        # maxSoFar is updated every iteration after determining max between the best previous subarray sum and current value
        
        # Any time maxSoFar is greater than maxSum, maxSum is updated
        
        # This strategy guarantees that at the end of the array, a global max has been determined
        for i in range(1,len(nums)):
            maxSumSoFar = max(maxSumSoFar+nums[i], nums[i])
            if (maxSumSoFar > maxSum):
                maxSum = maxSumSoFar
                
        return maxSum
