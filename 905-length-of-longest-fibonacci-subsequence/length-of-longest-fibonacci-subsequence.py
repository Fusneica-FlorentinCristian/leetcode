class Solution:
    def lenLongestFibSubseq(self, arr: list[int]) -> int:
        set_arr = set(arr)
        found = False
        max_count = 0
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                fib2 = arr[j]
                fib3 = arr[i] + fib2
                counter = 2
                while fib3 in set_arr:
                    found = True
                    counter += 1
                    fib2, fib3 = fib3, fib2 + fib3
                max_count = max(max_count, counter)
        if not found:
            return 0
        return max_count