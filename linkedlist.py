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

# This linked list does not store the nextFree variable
# Yet it still uses an array to store the nodes
# Its advantage is that this linked list can contain any number of nodes
# Its disadvantage is that you cannot remove from this linked list                
class LinkedListUncapped:
    def __init__(self):
        self.array = []
        self.start = -1
    
    def isEmpty(self):
        return self.start == -1
    
    def insert(self, value):
        newNode = Node()
        newNode.value = value
        self.array.append(newNode)
        # this new node has index len(self.array) - 1
        
        if self.isEmpty():
            newNode.next = -1
            self.start = 0
        elif value < self.array[self.start].value:
            newNode.next = self.start
            self.start = len(self.array) - 1
        else:
            current = self.start
            while current != -1 and self.array[current].value <= value:
                previous = current
                current = self.array[current].next
            newNode.next = current
            self.array[previous].next = len(self.array) - 1
    
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
                
    def display(self):
        if not self.isEmpty():
            current = self.start
            while current != -1:
                print(self.array[current].value)
                current = self.array[current].next

# This linked list does not use array to store nodes
# Its advantage is that this linked list can contain any number of nodes
# Yet, it can still allow remove freely
class NodeNative:
    def __init__(self):
        self.value = None
        self.next = None

class LinkedListNative:
    def __init__(self):
        self.start = None
    
    def isEmpty(self):
        return self.start == None
    
    def insert(self, value):
        newNode = NodeNative()
        newNode.value = value
        
        if self.isEmpty():
            newNode.next = None
            self.start = newNode
        elif value < self.start.value:
            newNode.next = self.start
            self.start = newNode
        else:
            current = self.start
            while current != None and current.value <= value:
                previous = current
                current = current.next
            newNode.next = current
            previous.next = newNode
    
    def search(self, value):
        if self.isEmpty():
            return False  # not found
        else:
            current = self.start
            while current != None and current.value < value:
                current = current.next
            if current != None and current.value == value:
                return True  # found
            else:
                return False  # not found
                
    def remove(self, value):
        if self.isEmpty():
            return False  # not found
        elif self.start.value == value:
            self.start = self.start.next
            return True  # found
        else:
            current = self.start
            while current != None and current.value < value:
                previous = current
                current = current.next
            if current != None and current.value == value:
                previous.next = current.next
                return True  # found
            else:
                return False  # not found
                
    def display(self):
        if not self.isEmpty():
            current = self.start
            while current != None:
                print(current.value)
                current = current.next
