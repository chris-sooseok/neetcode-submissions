class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed), reverse=True)
        # arrival time of each fleet
        stack = []

        for p, s in cars:
            time = (target - p) / s
            if not stack or time > stack[-1]:
                stack.append(time)
            # else: it catches up and merges, so we don't add anything

        return len(stack)
