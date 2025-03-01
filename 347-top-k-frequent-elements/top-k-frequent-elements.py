class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1 = defaultdict(int)
        for x in nums:
            d1[x] += 1

        reverse_d = defaultdict(list)
        for key, v in d1.items():
            reverse_d[v].append(key)
        answer = []
        counter = 0
        for i in list(reversed(range(len(nums) + 1))):
            for x in reverse_d[i]:
                answer.append(x)
                counter += 1
                if counter == k:
                    return answer