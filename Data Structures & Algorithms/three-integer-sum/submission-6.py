class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        ans = []
        print(nums)
        for xi, x in enumerate(nums):
            if x > 0:
                break
            if xi >= 1 and nums[xi-1] == nums[xi]:
                continue

            yi, zi = xi + 1, len(nums) - 1

            print(xi, yi, zi)

            while yi < zi:
                total = nums[xi] + nums[yi] + nums[zi]
                if nums[xi] + nums[yi] + nums[zi] < 0:
                    yi += 1
                    continue
                elif nums[xi] + nums[yi] + nums[zi] > 0:
                    zi -= 1
                    continue
                else:
                    ans.append([nums[xi], nums[yi], nums[zi]])
                    yi += 1
                    zi -= 1
                
                while nums[yi-1] == nums[yi] and yi < zi:
                    yi += 1

        return ans
                
