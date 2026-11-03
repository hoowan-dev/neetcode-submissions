class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars = sorted(cars, key=lambda x: x[0], reverse=True)

        fleetStack = []
        for car in cars:
            fleetStack.append((target - car[0]) / car[1])
            if len(fleetStack) >= 2 and fleetStack[-1] <= fleetStack[-2]:
                fleetStack.pop()

        return len(fleetStack)