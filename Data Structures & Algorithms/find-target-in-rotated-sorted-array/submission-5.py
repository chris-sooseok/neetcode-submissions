class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            # left is sorted
            if nums[l] <= nums[m]:
                # if true, left half
                # otherwise, right half
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # right is sorted
            else:
                # if ture, right half
                # otherwise, left half
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1