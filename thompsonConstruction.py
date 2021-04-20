# Author: Cory O'Donoghue
# Graph Theory Project
# Reference Dr.Ian McLoughlin https://web.microsoftstream.com/video/4012d43a-bb46-4ceb-8aa9-2ae598539a32

from shuntingre import *

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
    """An automaton"""
    def __init__(self, start, end):
        #Start state of the automaton.
        self.start = start
        self.end = end

    def match(regex, s):
    #Compile omto NFA
        nfa = re_to_nfa(regex)

    #Match the string to the text file string(s)
    #Current states
        current = set()
        followes(nfa.start, current)
    #Previous states
        previous = set()

    #Loof through characters
        for c in s:
        #state we are in
            previous = current
        #create a new state
            current = set()
        #Loop previous state
            for state in previous:
            #Follow arrows
                if state.label is not None:
                #See if it is equal
                    if state.label == c:
                #add at end of arrow to current state
                        followes(state.arrows[0], current)
    #return the output
        return nfa.end in current


def followes(state, current):
     if state not in current:
       #Current state
        current.add(state)
       #State label check
        if state.label is None:
            #loop through
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
            #start = State(None, [], False)
            end = State(None, [], True)
            # Make new start state point at old start states.
            start.arrows.append(nfa1.start)
            start.arrows.append(nfa2.start)
            # Make old end states non-accept.
            #nfa1.end.accept = False
            #nfa2.end.accept = False
            # Point old end states to new one.
            nfa2.end.arrows.append(end)
            nfa1.end.arrows.append(end)
            # Make a new NFA.
            nfa = NFA(nfa2.start, nfa1.end)
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
            nfa1 = stack[-1]
            stack = stack[:-1]
            start = State(None, [], False)
            end = State(None, [], True)
            start.arrows.append(nfa1.start)
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
        #newNFA = NFA(start, end)
        #stack.append(newNFA)
    # There should only be one NFA on the stack.
    return stack.pop()

if __name__ == "__main__":
    for postfix in ["abb.*.a.", "100.*.1.", 'ab|']:
        print(f"postfix: {postfix}")
        print(f"nfa:     {re_to_nfa(postfix)}")
        print()