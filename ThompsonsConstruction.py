#Thompsons construction

class State():
    """A state and its arrows in thompsons construction"""
    def __init__(self,label,arrows, accept):
        self.label = label
        self.arrows = arrows
        self.accept = accept

#represents NFA 
class NFA:
    """Non deterministic finite automation"""

    def __init__(self,start,end):
        self.start = start 
        self.end = end
    

def re_to_nfa(postfix):
    #stack for NFAs
    stack = []
    #Loop through the postfix r.e left to right
    for c in postfix:
        if c == '.':
            #pop top nfa off stack-first one you pop off goes to the right
            nfa2 = stack[-1]
            stack = stack[:-1]
            #pop left NFA off stack
            nfa1 = stack[-1]
            stack = stack[:-1]
            #Take accept state from nfa1(left)
            nfa1.end.accept = False
            #Make it point at the start state of NFA2
            nfa1.end.arrows = [nfa2.start]
            #make new NFA
            nfa = NFA(start=nfa1.start, end=nfa2.end)
            #push to the stack
            stack.append(nfa)

        elif c == '|':
             #pop top nfa off stack-first one you pop off goes to the right
            nfa2 = stack[-1]
            stack = stack[:-1]
            #pop left NFA off stack
            nfa1 = stack[-1]
            stack = stack[:-1]
            #Create new start and end states
            start = State(label=None, arrows=[], accept=False)
            end = State(label = None,arrows=[],accept =True)
            #make new start state point at old start states
            start.arrows.append(nfa1.start)
            start.arrows.append(nfa2.start)
            #Take accept state from nfa1(left)
            nfa1.end.accept = False
            nfa2.end.accept = False
            #make new NFA with with nfa1 start start state and nfas end state
            nfa = NFA(start=nfa1.start, end=nfa2.end)
            #push to the stack
            stack.append(nfa)
   
        elif c == '*':
            #pop one nfa off stack-first one you pop off goes to the right
            nfa1 = stack[-1]
            stack = stack[:-1]
            #Create new start and end states
            start = State(label=None, arrows=[], accept=False)
            end = State(label = None,arrows=[],accept =True)
            #make new start state point at old start states
            start.arrows.append(nfa1.start)
            #and at new end state
            start.arrows.append(end)
            #Take accept state from nfa1(left)
            nfa1.end.accept = False
            #make old accept state point to new end state
            nfa1.end.arrows.append(end)
            #make old accept state point to new end state
            nfa1.end.arrows.append(nfa1.start)
            #make a new NFA
            nfa = NFA(start,end)
            #push to the stack
            stack.append(nfa)
        else:
            #create an NFA for non special charcater c
            #creating end state
            end = State(label=None,arrows=[], accept = True)
             #creating start state
            start = State(label=c, arrows=[end], accept=False)
            #create nfa with start anf end state
            nfa = NFA(start=start,end=end)
            stack.append(nfa)
        

#checks if ive been running it as a script , if so run these tests
#if it is imported to another script dont run
if __name__ == "__main__":
    for postfix in ["abb.a*.a","100.*.1."]:
        print(f"postfix:   {postfix}")
        print(f"nfa: {re_to_nfa(postfix)}")
        print()