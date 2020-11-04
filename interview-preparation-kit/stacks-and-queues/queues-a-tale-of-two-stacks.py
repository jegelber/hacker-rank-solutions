# Score: 30/30

# Build a queue class from two stacks.
# Include enqueue, dequeue, and peek methods.

# Queue ADT is FIFO.

# q = [4, 7, 2, 9]

class MyQueue:
    def __init__(self):
        self.forward = []
        self.backward = []

    def peek(self):
        if len(self.forward) == 0 and len(self.backward) == 0:
            return "Error: Queue empty."
        elif len(self.backward) == 0:
            return self.forward[0]
        else:
            return self.backward[-1]

    def pop(self):
        if len(self.forward) == 0 and len(self.backward) == 0:
            return "Error: Queue empty."
        elif len(self.backward) == 0:
            while len(self.forward) != 0:
                temp = self.forward.pop()
                self.backward.append(temp)
            return self.backward.pop()
        else:
            return self.backward.pop()

    def push(self, value): # Runtime: O(1)
        self.forward.append(value)
