class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        map = {}
        cnts = []

        for num in nums:
            map[num] = True
        
        for k in map.keys():
            # if prev num dones't exist, start counting
            if map.get(k-1, "true") == "true":
                start = k
                cnt = 0 # start from 0
                # count until next number dones't exist 
                while map.get(start, "false") != "false":
                    cnt += 1
                    # invalidate each encountering num, so above if check can skip
                    map[start] = False
                    start += 1
                cnts.append(cnt)

        if cnts:
            return max(cnts)
        else:
            return 0



