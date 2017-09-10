class StackArray:
    def __init__(self, size = 20):
        self.array = [None] * 20
        self.top = -1
    
    def isFull(self):
        return self.top == len(self.array) - 1
    
    def isEmpty(self):
        return self.top == -1
        
    def length(self):
        return self.top + 1
        
    def push(self, value):
        if not self.isFull():
            self.top = self.top + 1
            self.array[self.top] = value
            
    def pop(self):
        if not self.isEmpty():
            self.top = self.top - 1
            return self.array[self.top + 1]
            
    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
            
    def display(self):  # from top
        for i in range(self.top, -1, -1):
            print(self.array[i])
            
class Node:
    def __init__(self):
        self.value = None
        self.next = -1

class StackLinkedList:
    def __init__(self, size = 20):
        self.array = [Node() for i in range(size)]
        self.top = -1
        self.len = 0
        self.nextFree = 0
        for i in range(size - 1):
            self.array[i].next = i + 1

    def isFull(self):
        return self.nextFree == -1
    
    def isEmpty(self):
        return self.top == -1
        
    def length(self):
        return self.len
        
    def push(self, value):
        if not self.isFull():
            current = self.nextFree
            self.array[current].value = value
            self.nextFree = self.array[current].next
            self.array[current].next = self.top
            self.top = current
            self.len = self.len + 1
            
    def pop(self):
        if not self.isEmpty():
            current = self.top
            self.top = self.array[current].next
            self.array[current].next = self.nextFree
            self.nextFree = current
            self.len = self.len - 1
            return self.array[current].value
            
    def peek(self):
        if not self.isEmpty():
            return self.array[self.top].value
            
    def display(self):  # from top
        if not self.isEmpty():
            current = self.top
            while current != -1:
                print(self.array[current].value)
                current = self.array[current].next
