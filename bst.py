class Node:
    def __init__(self):
        self.value = None
        self.left = -1
        self.right = -1

class BinarySearchTree:
    def __init__(self, size = 20):
        self.array = [Node() for i in range(size)]
        self.start = -1
        self.nextFree = 0
        for i in range(size - 1):
            self.array[i].right = i + 1
            
    def isFull(self):
        return self.nextFree == -1
    
    def isEmpty(self):
        return self.start == -1
            
    def insert(self, value):
        if not self.isFull():
            newNode = self.nextFree
            self.array[newNode].value = value
            self.nextFree = self.array[newNode].right
            self.array[newNode].left = -1
            self.array[newNode].right = -1

            if self.isEmpty():
                self.start = newNode
            else:
                current = self.start
                while current != -1:
                    previous = current
                    if self.array[current].value > value:
                        dir = "L"
                        current = self.array[current].left
                    else:
                        dir = "R"
                        current = self.array[current].right
                if dir == "L":
                    self.array[previous].left = newNode
                else:
                    self.array[previous].right = newNode
                    
    def searchIterative(self, value):
        if self.isEmpty():
            return -1  # not found
        else:
            current = self.start
            found = False
            while found == False and current != -1:
                if self.array[current].value == value:
                    found = True
                elif self.array[current].value > value:
                    current = self.array[current].left
                else:
                    current = self.array[current].right
            if found == True:
                return current
            else:
                return -1  # not found

    def searchRecursive(self, value, current = None):
        if current == None:
            current = self.start
        if current == -1:
            return -1
        elif self.array[current].value == value:
            return current
        elif self.array[current].value > value:
            return self.searchRecursive(value, self.array[current].left)
        else:
            return self.searchRecursive(value, self.array[current].right)
            
    def printInorder(self, current = None):
        if current == None:
            current = self.start
        if current != -1:
            self.printInorder(self.array[current].left)
            print(self.array[current].value)
            self.printInorder(self.array[current].right)
            
    def printPreorder(self, current = None):
        if current == None:
            current = self.start
        if current != -1:
            print(self.array[current].value)
            self.printPreorder(self.array[current].left)
            self.printPreorder(self.array[current].right)
            
    def printPostorder(self, current = None):
        if current == None:
            current = self.start
        if current != -1:
            self.printPostorder(self.array[current].left)
            self.printPostorder(self.array[current].right)
            print(self.array[current].value)
