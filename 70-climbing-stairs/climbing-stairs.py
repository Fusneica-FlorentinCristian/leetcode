class Solution:
    def climbStairs(self, n: int) -> int:
        pos = [0] * (n + 1)
        pos[0] = pos[1] = 1

        for i in range(2, n + 1):
            pos[i] = pos[i-1] + pos[i-2]
        
        return pos[n]