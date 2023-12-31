class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        collect = {}
        for n in nums:
            if n in collect:
                collect[n] += 1
            else:
                collect[n] = 1
        ans = []
        for x in range(k):
            top_x = max(collect, key=collect.get)
            ans.append(top_x)
            del collect[top_x]
        return ans