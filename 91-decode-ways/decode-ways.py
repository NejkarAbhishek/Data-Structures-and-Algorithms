class Solution:
    def numDecodings(self, s: str) -> int:

        n = len(s)
        memo = [-1] * (n + 1)
        
        def count(i):    

            if i == len(s):
                return 1
            
            if s[i] == '0':
                return 0
            
            if memo[i] != -1:
                return memo[i]

            ways = count(i + 1)

            if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                ways += count(i + 2)

            memo[i] = ways
            return ways

        return count(0)