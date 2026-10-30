class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        for i in range(n):
            for j in range(i+1, n):
                ans[j] = ans[j] * nums[i]

        for i in range(n-1, -1, -1):
            for j in range(i-1, -1, -1):
                ans[j] = ans[j] * nums[i]
        
        return ans