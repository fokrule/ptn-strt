from typing import List
class Even:
    def __init__(self, number):
        self.number = number

    def getEven(self)->List[int]:
        events = []
        ranges = []
        for i, value in enumerate(self.number):
            ranges.append(i)
            if value % 2 == 0:
                events.append(value)
        return events

even = Even([2,3,4,5,6,7])
print(even.getEven())

