class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            # Left half [l..m] is sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1   # target is in the sorted left half
                else:
                    l = m + 1   # otherwise go right
            # Right half [m..r] is sorted
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1   # target is in the sorted right half
                else:
                    r = m - 1   # otherwise go left

        return -1