class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                # take upper limit
                hours += math.ceil(p / k)

            # k is fast enough, so try a slower speed
            if hours <= h:
                res = k
                r = k - 1
            # too slow, so she needs a faster speed
            else:
                l = k + 1

        return res