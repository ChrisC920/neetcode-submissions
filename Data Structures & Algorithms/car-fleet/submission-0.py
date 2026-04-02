class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        count = 0

        for pos, speed in pair:
            time = (target - pos) / speed
            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)
                count += 1
        return count