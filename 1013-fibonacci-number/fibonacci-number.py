class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        fibl = [0] * (n + 1)
        fibl[1] = 1
        for i in range(2, n + 1):
            fibl[i] = fibl[i - 1] + fibl[i - 2]
        return fibl[n]
