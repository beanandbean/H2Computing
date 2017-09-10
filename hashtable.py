# separated functions

def insert(array, value):
    index = value % len(array)
    if array[index] != None:
        begin = index
        index = (index + 1) % len(array)
        while index != begin and array[index] != None:
            index = (index + 1) % len(array)
    if array[index] != None:
        return False  # table full
    else:
        array[index] = value
        return True  # inserted
        
def search(array, value):
    index = value % len(array)
    if array[index] != None and array[index] != value:
        begin = index
        index = (index + 1) % len(array)
        while index != begin and array[index] != None and array[index] != value:
            index = (index + 1) % len(array)
    if array[index] == value:
        return index
    else:
        return -1  # not found

# class form

class HashTable:
    def __init__(self, size):
        self.array = [None] * size
        
    def insert(self, value):
        index = value % len(self.array)
        if self.array[index] != None:
            begin = index
            index = (index + 1) % len(self.array)
            while index != begin and self.array[index] != None:
                index = (index + 1) % len(self.array)
        if self.array[index] != None:
            return False  # table full
        else:
            self.array[index] = value
            return True  # inserted
            
    def search(self, value):
        index = value % len(self.array)
        if self.array[index] != None and self.array[index] != value:
            begin = index
            index = (index + 1) % len(self.array)
            while index != begin and self.array[index] != None and self.array[index] != value:
                index = (index + 1) % len(self.array)
        if self.array[index] == value:
            return index
        else:
            return -1  # not found
