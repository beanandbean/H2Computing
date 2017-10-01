# Queues in this file all pushes to head, and pops from tail

class QueueArrayCircular:
    def __init__(self, size = 20):
        self.array = [None] * 20
        self.head = -1
        self.len = 0
    
    def isFull(self):
        return self.len == len(self.array)
    
    def isEmpty(self):
        return self.len == 0
        
    def length(self):
        return self.len
        
    def push(self, value):
        if not self.isFull():
            self.head = (self.head + 1) % 20
            self.len = self.len + 1
            self.array[self.head] = value
            
    def pop(self):
        if not self.isEmpty():
            self.len = self.len - 1
            return self.array[self.head - self.len]
            
    def peek(self):
        if not self.isEmpty():
            return self.array[self.head - self.len + 1]
            
    def display(self):  # from tail to head
        for i in range(self.len - 1, -1, -1):
            print(self.array[self.head - i])

# This is an non-circular implementation
# It's less time efficient, but can contain any number of values
class QueueArray:
	def __init__(self):
		self.array = []
	
	def isEmpty(self):
		return len(self.array) == 0
		
	def length(self):
		return len(self.array)
		
	def push(self, value):
		self.array.append(value)
			
	def pop(self):
		if not self.isEmpty():
			return self.array.pop(0)
			
	def peek(self):
		if not self.isEmpty():
			return self.array[0]
			
	def display(self):	# from tail to head
		for value in self.array:
			print(value)

class Node:
    def __init__(self):
        self.value = None
        self.next = -1

class QueueLinkedList:
    def __init__(self, size = 20):
        self.array = [Node() for i in range(size)]
        self.head = -1
        self.tail = -1
        self.len = 0
        self.nextFree = 0
        for i in range(size - 1):
            self.array[i].next = i + 1

    def isFull(self):
        return self.nextFree == -1
    
    def isEmpty(self):
        return self.head == -1
        
    def length(self):
        return self.len
        
    def push(self, value):
        if not self.isFull():
            current = self.nextFree
            self.array[current].value = value
            self.nextFree = self.array[current].next
            self.array[current].next = -1
            if self.isEmpty():
                self.tail = current
            else:
                self.array[self.head].next = current
            self.head = current
            self.len = self.len + 1
            
    def pop(self):
        if not self.isEmpty():
            current = self.tail
            self.tail = self.array[current].next
            if self.tail == -1:
                self.head = -1
            self.array[current].next = self.nextFree
            self.nextFree = current
            self.len = self.len - 1
            return self.array[current].value
            
    def peek(self):
        if not self.isEmpty():
            return self.array[self.tail].value
            
    def display(self):  # from tail to head
        if not self.isEmpty():
            current = self.tail
            while current != -1:
                print(self.array[current].value)
                current = self.array[current].next

# This is the linked list implementation without using array of nodes
# It is an time-efficient implementation that allows any number of nodes
class NodeNative:
    def __init__(self):
        self.value = None
        self.next = None

class QueueLinkedListNative:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0
    
    def isEmpty(self):
        return self.head == None
        
    def length(self):
        return self.len
        
    def push(self, value):
        current = NodeNative()
        current.value = value
        current.next = None
        if self.isEmpty():
            self.tail = current
        else:
            self.head.next = current
        self.head = current
        self.len = self.len + 1
            
    def pop(self):
        if not self.isEmpty():
            current = self.tail
            self.tail = current.next
            if self.tail == None:
                self.head = None
            self.len = self.len - 1
            return current.value
            
    def peek(self):
        if not self.isEmpty():
            return self.tail.value
            
    def display(self):  # from tail to head
        if not self.isEmpty():
            current = self.tail
            while current != None:
                print(current.value)
                current = current.next
