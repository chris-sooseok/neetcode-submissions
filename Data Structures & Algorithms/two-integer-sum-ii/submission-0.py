class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        seen = {} # num : idx

        for idx, n in enumerate(numbers):
            c = target - n
            if c in seen:
                return [seen[c]+1,idx+1]
            seen[n] = idx
        