class Node:
    def __init__(self):
        self.value = None
        self.next = -1

class LinkedList:
    def __init__(self, size = 20):
        self.array = [Node() for i in range(size)]
        self.start = -1
        self.nextFree = 0
        for i in range(size - 1):
            self.array[i].next = i + 1
            
    def isFull(self):
        return self.nextFree == -1
    
    def isEmpty(self):
        return self.start == -1
    
    def insert(self, value):
        if not self.isFull():
            newNode = self.nextFree
            self.array[newNode].value = value
            self.nextFree = self.array[newNode].next
            
            if self.isEmpty():
                self.array[newNode].next = -1
                self.start = newNode
            elif value < self.array[self.start].value:
                self.array[newNode].next = self.start
                self.start = newNode
            else:
                current = self.start
                while current != -1 and self.array[current].value <= value:
                    previous = current
                    current = self.array[current].next
                self.array[newNode].next = current
                self.array[previous].next = newNode
    
    def search(self, value):
        if self.isEmpty():
            return -1  # not found
        else:
            current = self.start
            while current != -1 and self.array[current].value < value:
                current = self.array[current].next
            if current != -1 and self.array[current].value == value:
                return current
            else:
                return -1  # not found
                
    def remove(self, value):
        if self.isEmpty():
            return -1  # not found
        elif self.array[self.start].value == value:
            current = self.start
            self.start = self.array[self.start].next
            self.array[current].next = self.nextFree
            self.nextFree = current
            return current
        else:
            current = self.start
            while current != -1 and self.array[current].value < value:
                previous = current
                current = self.array[current].next
            if current != -1 and self.array[current].value == value:
                self.array[previous].next = self.array[current].next
                self.array[current].next = self.nextFree
                self.nextFree = current
                return current
            else:
                return -1  # not found
                
    def display(self):
        if not self.isEmpty():
            current = self.start
            while current != -1:
                print(self.array[current].value)
                current = self.array[current].next
