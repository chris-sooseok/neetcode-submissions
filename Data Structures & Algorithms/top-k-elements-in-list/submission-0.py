class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        cnt = {}

        for n in nums:
            cnt[n] = 1 + cnt.get(n, 0)
        
        sorted_cnt = sorted(cnt, key=cnt.get)

        return sorted_cnt[-k:]