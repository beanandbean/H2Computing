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
            while current != -1 and self.array[current].value != value:
                if self.array[current].value > value:
                    current = self.array[current].left
                else:
                    current = self.array[current].right
            return current  # -1 for not found

    def searchRecursive(self, value, current = None):
        if current == None:
            current = self.start
        if current == -1 or self.array[current].value == value:
            return current  # -1 for not found
        elif self.array[current].value > value:
            return self.searchRecursive(value, self.array[current].left)
        else:
            return self.searchRecursive(value, self.array[current].right)
                        
    def remove(self, value):
        if self.isEmpty():
            found = -1  # not found
        elif self.array[self.start].value == value:
            found = self.start
            parent = self.array[self.start].left
            right = self.array[self.start].right
            if parent != -1:
                self.start = parent
                left = self.array[parent].right
            else:
                self.start = right
        else:
            found = self.start
            while found != -1 and self.array[found].value != value:
                previous = found
                if self.array[found].value > value:
                    dir = "L"
                    found = self.array[found].left
                else:
                    dir = "R"
                    found = self.array[found].right
                    
            if found != -1:
                parent = self.array[found].left
                right = self.array[found].right
                if dir == "L":
                    if parent != -1:
                        self.array[previous].left = parent
                        left = self.array[parent].right
                    else:
                        self.array[previous].left = right
                else:
                    if parent != -1:
                        self.array[previous].right = parent
                        left = self.array[parent].right
                    else:
                        self.array[previous].right = right
                        
        if found != -1:
            if parent != -1:
                while left != -1:
                    self.array[parent].right = left
                    parent = left
                    left = self.array[parent].left
                self.array[parent].right = right
            self.array[found].right = self.nextFree
            self.nextFree = found
        return found  # -1 for not found
                        
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

# This is the tree implementation without using array of nodes
# Its advantage is that it can contain any number of nodes
class NodeNative:
    def __init__(self):
        self.value = None
        self.left = None
        self.right = None

class BinarySearchTreeNative:
    def __init__(self):
        self.start = None
    
    def isEmpty(self):
        return self.start == None
            
    def insert(self, value):
        newNode = NodeNative()
        newNode.value = value
        newNode.left = None
        newNode.right = None

        if self.isEmpty():
            self.start = newNode
        else:
            current = self.start
            while current != None:
                previous = current
                if current.value > value:
                    dir = "L"
                    current = current.left
                else:
                    dir = "R"
                    current = current.right
            if dir == "L":
                previous.left = newNode
            else:
                previous.right = newNode
                    
    def searchIterative(self, value):
        if self.isEmpty():
            return False  # not found
        else:
            current = self.start
            while current != None and current.value != value:
                if current.value > value:
                    current = current.left
                else:
                    current = current.right
            if current == None:
                return False  # not found
            else:
                return True  # found

    def searchRecursive(self, value, current = "START"):
        if current == "START":
            current = self.start
        if current == None:
            return False  # not found
        elif current.value == value:
            return True  # found
        elif current.value > value:
            return self.searchRecursive(value, current.left)
        else:
            return self.searchRecursive(value, current.right)
                        
    def remove(self, value):
        if self.isEmpty():
            found = None  # not found
        elif self.start.value == value:
            found = self.start
            parent = self.start.left
            right = self.start.right
            if parent != None:
                self.start = parent
                left = parent.right
            else:
                self.start = right
        else:
            found = self.start
            while found != None and found.value != value:
                previous = found
                if found.value > value:
                    dir = "L"
                    found = found.left
                else:
                    dir = "R"
                    found = found.right
                    
            if found != None:
                parent = found.left
                right = found.right
                if dir == "L":
                    if parent != None:
                        previous.left = parent
                        left = parent.right
                    else:
                        previous.left = right
                else:
                    if parent != None:
                        previous.right = parent
                        left = parent.right
                    else:
                        previous.right = right
                        
        if found != None:
            if parent != None:
                while left != None:
                    parent.right = left
                    parent = left
                    left = parent.left
                parent.right = right
            return True  # found
        else:
            return False  # not found
                        
    def printInorder(self, current = "START"):
        if current == "START":
            current = self.start
        if current != None:
            self.printInorder(current.left)
            print(current.value)
            self.printInorder(current.right)
            
    def printPreorder(self, current = "START"):
        if current == "START":
            current = self.start
        if current != None:
            print(current.value)
            self.printPreorder(current.left)
            self.printPreorder(current.right)
            
    def printPostorder(self, current = "START"):
        if current == "START":
            current = self.start
        if current != None:
            self.printPostorder(current.left)
            self.printPostorder(current.right)
            print(current.value)
