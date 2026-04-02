class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars = list(reversed(sorted(cars, key=lambda x: x[0])))

        print(cars)

        stack = []

        for i in range(len(cars)):
            pos, speed = cars[i]
            time = (target - pos) / speed
            if stack and stack[-1] >= time:
                stack[-1] = max(time, stack[-1])
            else:
                stack.append(time)


        return len(stack)