from typing import List, Optional

class Solution:
    def evaluate(self, expression: str) -> int:
        stack = []
        pos = 0
        n = len(expression)
        
        while pos < n:
            char = expression[pos]
            
            # Case 1: Addition Operator
            if char == 'a':
                stack.append("add")
                pos += 4  # Skip the exact characters "add("
                
            # Case 2: Subtraction Operator
            elif char == 's':
                stack.append("sub")
                pos += 4  # Skip the exact characters "sub("
                
            # Case 3: Closing Parenthesis triggers evaluation
            elif char == ')':
                # The top of the stack has our two operands and the operator
                val2 = stack.pop()
                val1 = stack.pop()
                op = stack.pop()
                
                # Compute and push the result back onto the stack
                if op == "add":
                    stack.append(val1 + val2)
                elif op == "sub":
                    stack.append(val1 - val2)
                    
                pos += 1 # Move past the ')'
                
            # Case 4: Integer Parsing (Handles negative signs and multi-digit numbers)
            elif char == '-' or char.isdigit():
                sign = 1
                if char == '-':
                    sign = -1
                    pos += 1
                
                num = 0
                # Keep building the integer as long as we see digits
                while pos < n and expression[pos].isdigit():
                    num = num * 10 + int(expression[pos])
                    pos += 1
                    
                stack.append(sign * num)
                
            # Case 5: Spaces and Commas
            else:
                pos += 1
                
        # The final result is the only item left in the stack
        return stack[0]