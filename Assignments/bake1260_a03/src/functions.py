"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Benjamin Baker
ID:      169081260
Email:   bake1260@mylaurier.ca
__updated__ = "2025-01-22"
-------------------------------------------------------
"""
# Imports
from Stack_array import Stack
from pickle import NONE

# Constants
OPERATORS = "+-*/"

def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    target1 = Stack()
    target2 = Stack()
    index = 0

    while not source.is_empty():
        value = source.pop()

        if index % 2 == 0:
            target1.push(value)
        else:
            target2.push(value)

        index += 1

    return target1, target2

def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source stack into separate target stacks with values
        alternating into the targets. At finish source stack is empty.
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (Stack)
            target2 - contains other alternating values from source (Stack)
        -------------------------------------------------------
        """
        
        target1 = Stack()
        target2 = Stack()

        while not self.is_empty():
            target1.push(self._values.pop()) 
            if not self.is_empty():  
                target2.push(self._values.pop()) 

        return target1, target2
    
        
def stack_reverse(source):
    """
    -------------------------------------------------------
    Reverses the contents of a stack.
    Use: stack_reverse(source)
    -------------------------------------------------------
    Parameters:
        source - a Stack (Stack)
    Returns:
        None
    -------------------------------------------------------
    """

    temp_stack = Stack()
    
    while not source.is_empty():
        temp_stack.push(source.pop())

    while not temp_stack.is_empty():
        source.push(temp_stack.pop())
        
        return None
    
def reverse(self):
        """
        -------------------------------------------------------
        Reverses the contents of the source stack.
        Use: source.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        
        self._values = self._values[::-1]
        
        return None

def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    
    string = string.lower()
    string = ''.join(c for c in string if c.isalnum())

    stack = []
    for char in string:
        stack.append(char)

    while len(stack) > 1:
        if stack.pop(0) != stack.pop():
            return False

    return True
    
def postfix(string):
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    
    stack = []
    tokens = string.split()

    for token in tokens:
        if token not in OPERATORS:
            stack.append(float(token))
        else:
            # Pop the two operands
            operand2 = stack.pop()
            operand1 = stack.pop()

            # Evaluate the expression
            if token == "+":
                result = operand1 + operand2
            elif token == "-":
                result = operand1 - operand2
            elif token == "*":
                result = operand1 * operand2
            elif token == "/":
                result = operand1 / operand2

            # Push the result onto the stack
            stack.append(result)

    return stack.pop()

def reroute(opstring, values_in):
    """
    -------------------------------------------------------
    Reroutes values in a list according to a operating string and
    returns a new list of values. values_in is unchanged.
    In opstring, 'S' means push onto stack,
    'X' means pop from stack into values_out.
    Use: values_out = reroute(opstring, values_in)
    -------------------------------------------------------
    Parameters:
        opstring - String containing only 'S' and 'X's (str)
        values_in - A valid list (list of ?)
    Returns:
        values_out - if opstring is valid then values_out contains a
            reordered version of values_in, otherwise returns
            None (list of ?)
    -------------------------------------------------------
    """
    
    values_out = []
    stack = values_in.copy()

    for op in opstring:
        if op == 'S':  
            if stack:
                values_out.append(stack.pop(0))
            else:
                return None  
        elif op == 'X': 
            if values_out: 
                stack.insert(0, values_out.pop())
            else:
                return None  
    return values_out
