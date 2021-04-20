# Author: Cory O'Donoghue
# Graph Theory Project
# Reference Dr.Ian McLoughlin https://web.microsoftstream.com/video/4012d43a-bb46-4ceb-8aa9-2ae598539a32 for original thomspons construction video 2021
# Reference Dr.ian McLoughlin https://web.microsoftstream.com/video/f4bc3634-b94f-4c15-b2c1-70cccd874c54?list=user&userId=20b32719-41e8-4560-9f7f-c83ba751229c for matching & small changes to thompsons construction 2020
#Once I had completed all of your labs and began trying to implement my user functions calling match() from menu file, I was repeatedly gettin an error which was
"""==========Error ==========
previous = self.start.followes()
AttributeError: 'str' object has no attribute start"""
#I then watched back your video from the previous year where I took the match(), and added minor changes to the thompson which staright away worked with my function


from shuntingre import shunt

class State:
    """A state and its arrows in Thompson's construction."""
    def __init__(self, label, arrows, accept):
        """label is the arrow labels, arrows is a list of states to
           point to, accept is a boolean as to whether this is an accept
           state.
        """
        self.label = label
        self.arrows = arrows
        self.accept = accept


class NFA:
   """A non-deterministic finite automaton."""
   def __init__(self, start, end):
        #Start state of the automaton.
        self.start = start
        self.end = end

   def match(regex,s):
        #Compile onto NFA
        nfa = re_to_nfa(regex)

       # Try to match the regular expression to the string s
       # The Current set of states
        current = set()
        followes(nfa.start, current)
       #Previous set of states
        previous = set()

        #Loop through characters in s
        for c in s:
        #Keep track of where we were
            previous = current
         # Create a new empty set for states we're about to be in.
            current = set()
        #Loop through previous state
            for state in previous:
            #Follow arrows
                if state.label is not None:
                #See if it is equal
                    if state.label == c:
                #add at end of arrow to current state
                        followes(state.arrows[0], current)

    #return the output
        return nfa.end in current

#Add a state to set and follow all e arrows
def followes(state, current):
     if state not in current:
       #Put state into current
        current.add(state)
       #State label check
        if state.label is None:
            #loop through states pointed by this one
            for x in state.arrows:
                #call result
                followes(x, current)


def re_to_nfa(infix):
    # A stack for NFAs.
    postfix = shunt(infix)
    postfix = list(postfix)[::-1]
    stack = []
    # Loop through the postfix r.e. left to right.
    while postfix:
        c = postfix.pop()
        # Concatenation.
        if c == '.':
          # Pop top NFA off stack.
            nfa2 = stack[-1]
            stack = stack[:-1]
            # Pop the next NFA off stack.
            nfa1 = stack[-1]
            stack = stack[:-1]
            # Make accept state of NFA1 non-accept.
            nfa1.end.accept = False
            # Make it point at start state of nfa2.
            nfa1.end.arrows.append(nfa2.start)
            # Make a new NFA with nfa1's start state and nfa2's end state.
            nfa = NFA(nfa1.start, nfa2.end)
            # Push to the stack.
            stack.append(nfa)
        elif c == '|':
            # Pop top NFA off stack.
            nfa2 = stack[-1]
            stack = stack[:-1]
            # Pop the next NFA off stack.
            nfa1 = stack[-1]
            stack = stack[:-1]
            # Create new start and end states.
            start = State(None, [], False)
            end = State(None, [], True)
            # Make new start state point at old start states.
            start.arrows.append(nfa1.start)
            start.arrows.append(nfa2.start)
            # Make old end states non-accept.
            nfa1.end.accept = False
            nfa2.end.accept = False
            # Point old end states to new one.
            nfa1.end.arrows.append(end)
            nfa2.end.arrows.append(end)
            # Make a new NFA.
            nfa = NFA(start, end)
            # Push to the stack.
            stack.append(nfa)
        elif c == '*':
          # Pop one NFA off stack.
            nfa1 = stack[-1]
            stack = stack[:-1]
            # Create new start and end states.
            start = State(None, [], False)
            end = State(None, [], True)
            # Make new start state point at old start state.
            start.arrows.append(nfa1.start)
            # And at the new end state.
            start.arrows.append(end)
            # Make old end state non-accept.
            nfa1.end.accept = False
            # Make old end state point to new end state.
            nfa1.end.arrows.append(end)
            # Make old end state point to old start state.
            nfa1.end.arrows.append(nfa1.start)
            # Make a new NFA.
            nfa = NFA(start, end)
            # Push to the stack.
            stack.append(nfa)
        elif c == '+':
             #Pop one NFA off stack
            nfa1 = stack[-1]
            stack = stack[:-1]
            #Create new start and end state
            start = State(None, [], False)
            end = State(None, [], True)
            #Make new start point at old start state
            start.arrows.append(nfa1.start)
            #and at the new end state
            nfa1.end.arrows.append(end)
            # Make old end state point to old start state.
            nfa1.end.arrows.append(nfa1.start)
            # Make a new NFA.
            nfa = NFA(start, end)
            # Push to the stack.
            stack.append(nfa)
        
        else:
            # Create an NFA for the non-special character c.
            # Create the end state.
            end = State(None, [], True)
            # Create the start state.
            start = State(c, [], False)
            # Point new start state at new end state.
            start.arrows.append(end)
            # Create the NFA with the start and end state.
            nfa = NFA(start, end)
            # Append the NFA to the NFA stack.
            stack.append(nfa)
        
    # There should only be one NFA on the stack.
    return stack.pop()

if __name__ == "__main__":
    for postfix in ["abb.*.a.", "100.*.1.", 'ab|']:
        print(f"postfix: {postfix}")
        print(f"nfa:     {re_to_nfa(postfix)}")
        print()