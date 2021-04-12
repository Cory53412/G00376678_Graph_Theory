#shunting yard algorithem
def shunt(infix):
     """Convert infix expressions to postfix."""
    # End output & algorithem stack.
     postfix = ""
     stack  = ""
    # declaring special operators and their priority in the stack
     specials = {'*':100 , '.':90, '|':80}   
    # Loop through the input a character at a time.
     for c in infix:
        # c is a digit.
        if c in {'a', 'b'}:
            # Push it to the output.
            postfix = postfix + c
        # c is an operator.
        elif c in {'*','.','|'}:
            # Check what is on the stack.
             while len(stack) > 0 and stack[-1] != '(' and specials[stack[-1]] >= specials[c]:
                # Append operator at top of stack to output.
                postfix = postfix + stack[-1]
                # Remove operator from stack.
                stack = stack[:-1]
             # Push c to stack.
             stack = stack + c
        elif c == '(':
            # Push c to stack.
            stack = stack + c
        elif c == ')':
            while stack[-1] != "(":
                # Append operator at top of stack to output.
                postfix = postfix + stack[-1]
                # Remove operator from stack.
                stack = stack[:-1]
            # Remove open bracket from stack.
            stack = stack[:-1]
         # Empty the operator stack.
     while len(stack) != 0:
        # Append operator at top of stack to output.
         postfix = postfix + stack[-1]
        # Remove operator from stack.
         stack = stack[:-1]
          # Return the postfix version of infix.
     return postfix


#checks if ive been running it as a script , if so run these tests
#if it is imported to another script dont run
if __name__ == "__main__":
    for infix in ["a.(b.b)*.a"]:
        print(f"infix:   {infix}")
        print(f"postfix: {shunt(infix)}")
        print()



