class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_area = 0
        i, j = 0, len(heights) - 1

        while i < j:
            # compute area every time and update max area
            w = j - i
            h = min(heights[i], heights[j])
            # print(f"width: {w}, height: {h}, area: {w*h}, cur_max: {max_area}")
            max_area = max(max_area, w*h)

            # on every loop, we decide which one should advance
            # we want possibly higher height, so lower one should move
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        
        return max_area