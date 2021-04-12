#shunting yard algorithem

def shunt(infix):
    """Converting the infix E.G-3+4x(2-1) regular expressions to postfic E.G 3421+xx-"""

   #end output
    postfix = ""

    #shunting yard algorithem stack
    stack=""

    # declaring special operators and their priority in the stack
    prec = {'*':100, '/':90, '+':80, '-':70}

    for c in infix:
         # c is a digit.
        if c in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
            # Push it to the output.
            postfix = postfix + c
        # c is an operator.
        elif c in {'+', '-', '*', '/'}:
            #check what is on the stack
            while len(stack) > 0 and stack[-1] != '(' and prec[stack[-1]] > prec[c]:
                #append operator at top of stack to output
                postfix = postfix + stack[-1]

                #remove operator from stack
                stack = stack[]
            
            #push c to stack
            stack = stack + c

