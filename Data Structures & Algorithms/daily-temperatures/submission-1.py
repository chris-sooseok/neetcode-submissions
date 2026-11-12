class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        n = len(temperatures)
        ans = [0] * n
        s = []

        for i in range(n-1, -1, -1):
            n = temperatures[i]
            # print("cur i, n:", i, n)

            if not s:
                s.append((i, n))
                continue
            
            while s:
                top = s[-1]
                # print(top)
                if n >= top[1]:
                    s.pop()
                else:
                    # print("found high temp. the index gap is:", top[0] - i)
                    ans[i] = top[0] - i
                    break
            
            s.append((i, n))
        
            # print("now the stack: ", s)
        return ans
            



