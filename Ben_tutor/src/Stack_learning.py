"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Baker
ID:      169081260
Email:   bake1260@mylaurier.ca
__updated__ = "2025-02-25"
-------------------------------------------------------
"""
class Stack:

    def __init__(self):
        self.item = []
        
    # Initializing an empty stack
    
    def is_empty(self):
        return len(self.item) == 0
    
    # Check if the stack is empty
    
    def push(self, item):
        self.items.append(item)
    
    # Add an item on the top of the stack (append = add at the end)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else: # Stack is Empty, cannot pop, raises an error
            raise IndexError ("stack is empty")
        
    # Removes Item from the top and then returns the item that it is removing
    
    def peek(self):        
        if not self.is_empty():
            return self.items[-1]
        else: # The stack is empty, cannot return top without removing, raise error
            print("stack is empty")
            raise IndexError("stack is empty")
    
    #Return the top without removing
    
    def size(self):
        return len(self.items)
    
    #Returns the Length of the self.item
    
    def _iter_(self):
        for value in self.items[::-1]: # Reverses the list
            yield value
            
    #Lets you use for loop to print one item of the stack at a time
    


