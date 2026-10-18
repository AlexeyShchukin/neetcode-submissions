class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        stack = []
        for p, s in cars:
            travel_time = (target - p) / s
            if not stack or travel_time > stack[-1]:
                stack.append(travel_time)
        return len(stack)