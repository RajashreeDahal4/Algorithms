"""
Date: January 30, 2024
Name: Rajashree Dahal
Problem: You are given an integer array coins representing coins of different denominations and an integer amount 
representing a total amount of money. Return the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int,dp=None) -> int:
        if dp is None:
            dp={}
            for each_coin in coins:
                dp[each_coin]=1  
            dp[0]=0
        backup=[]
        if amount in dp.keys():
            return dp[amount]
        for coin in coins:
            if amount>=coin:
                result=self.coinChange(coins,amount-coin,dp)
                if result==-1:
                    backup.append(result)
                else:
                    backup.append(result+1)
        backup=[i for i in backup if i!=-1]
        if backup:
            dp[amount]=min(backup)
        else:
            dp[amount]=-1
        return dp[amount]
