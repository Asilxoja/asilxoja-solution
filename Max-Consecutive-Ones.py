class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        # Create a list to store the number of distinct ways for each step
        dp = [0] * (n + 1)
        
        # Base cases
        dp[1] = 1
        dp[2] = 2
        
        # Calculate the number of distinct ways for each step
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
