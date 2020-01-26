class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # the overall problem is a series of subproblems: what is the least
        # number of coins to make change with?
        
        # bottom up approach
    
        # initially set return value to -1, to handle unsolveable case
        bestCoinChange = -1
        
         # initialize array with size amount + 1, for the 0th subproblem, with value greater than amount required to solve for, to represent unsolved case and allow min() to work
        tableSize = amount+1
        seenCoinChanges = [tableSize] * tableSize
        print(seenCoinChanges)
        
        # the least number of coins to make change for 0 is 0
        seenCoinChanges[0] = 0
        
        # at every iteration, determine the least number of coins for money amount = index
        # solve i subproblems from 1 to amount, index represents the subproblem "least coins to make index amount of change"
        for i in range(1, len(seenCoinChanges)):
            for coin in range(0, len(coins)):
                # determine if a coin can actually be used
                if ((i - coin) >= 0):
                    seenCoinChanges[i] = min(seenCoinChanges[i], seenCoinChanges[i-coins[coin]] + 1)
        
        if seenCoinChanges[amount] <= amount:
            bestCoinChange = seenCoinChanges[amount]
        return bestCoinChange
