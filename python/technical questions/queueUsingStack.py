# implement queue using stack
# stack - first in last out
# queue - fast in first out

class Queue:
    def __init__(self):
        self.input = []
        self.output = []
    
    def move(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
    
    def push(self, x):
        self.input.append(x)
    
    def pop(self):
        self.move()
        return self.output.pop()

    def peek(self):
        self.move()
        return self.output[-1]
    
    def empty(self):
        return len(self.input) == 0 and len(self.output) == 0

    def display(self):
        print("INPUT:", self.input)
        print("OUTPUT:", self.output)

q = Queue()
q.push(10)
q.push(20)

q.pop()
q.peek()

q.display()