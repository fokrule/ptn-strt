# from typing import List
# class Even:
#     def __init__(self, number):
#         self.number = number

#     def getEven(self)->List[int]:
#         events = []
#         ranges = []
#         for i, value in enumerate(self.number):
#             ranges.append(i)
#             if value % 2 == 0:
#                 events.append(value)
#         return events

# even = Even([2,3,4,5,6,7])
# print(even.getEven())

# class listFunction:
#     def listprint(self, numbers:list[int]):
#         numbers[2] = 42 # replace index 2 value
#         print("Second Index",numbers[2])
#         numbers.append(33) # add a new value at the end
#         for i in numbers:
#             print("after append 33",i)
#         numbers.remove(3) # remvoe value 3 not index 3
#         for i in numbers:
#             print("after removing 3", i)
#         numbers.insert(2, 56) # insert 56 at 2nd position and move all the indexes to the right from 2nd index
#         print(numbers[2])
#         numbers.pop() # remove last index
#         for i in numbers:
#             print("after pop",i)

# listFn = listFunction()
# listFn.listprint([2,3,1,4,5])


# reverse loop
def loop(numbers):
    print("regular loop")
    for num in numbers:
        print(num)
    print("reverse")
    for num in numbers[::-1]:
         print(num) 
    print("reverse with reverse keyword")
    for num in reversed(numbers):
         print(num)  
    print("reverse with range")
    lent = len(numbers)
    for num in range(lent-1, -1, -1):
         print(num)  
        
        
loop([3,4,5,6,7,8,9])



# stack code
def stackFunction(data):
    print("Initial stack",data)
    data.append(10)
    print("Modified stack",data)
    popdata = data.pop()
    print("Poped data", popdata)
    print("final data", data)

stackFunction([2,3,4,1])


from collection import deque

queue = deque()

queue.append(1)
queue.popleft()


