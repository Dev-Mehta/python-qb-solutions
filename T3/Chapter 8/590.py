"""
Stacks and Queues. Write a class SQ that defines a data structure that can behave as both a queue (FIFO) or a stack (LIFO), 
There are five methods that should be implemented:
1.	make a constructor with a valid parameter 
2.	shift() returns the first element and removes it from the list. Also, use the custom(raise) exception in this method.
3.	unshift() "pushes" a new element to the front or head of the list
4.	push() adds a new element to the end of a list
5.	pop() returns the last element and removes it from the list
6.	remove() returns the maximum element of the list and removes it from the list.
7.	Create the object and call all methods of the SQ class.
"""

class StackQueue:
    def __init__(self, queue: list):
        self.stack = queue

    def empty(self):
        return len(self.stack) == 0
    
    def shift(self):
        if not self.empty():
            x = self.stack[0]
            self.stack = self.stack[1:]
            return x
    def unshift(self, i: int):
        self.stack.insert(0, i)
    
    def push(self, x):
        self.stack.append(x)

    def pop(self):
        return self.stack.pop()
    
    def remove(self):
        x = max(self.stack)
        self.stack.remove(x)
        return x
    
    def __str__(self) -> str:
        return str(self.stack)

sq = StackQueue([1,4,6,10,12,14,16])
print(sq.shift())
sq.unshift(7)
sq.push(20)
print(f"Max: {sq.remove()}")
print(sq)
print(sq.pop())
print(sq.pop())
print(sq.pop())
print(sq)