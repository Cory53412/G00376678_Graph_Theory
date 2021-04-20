# Author: Cory O'Donoghue
# Graph Theory Project
import shuntingre , thompsonConstruction

def user_input():
    infixEntry = list(input("\nPlease enter a list or single infix expression: ").split()) 
    stringEntry = list(input("Please enter a list or single string: ").split()) 
    print_Input(infixEntry, stringEntry)

def infix_Examples():
    infixes = ["a.b.a*", "a.(b.b)*.a", "a.b.b+"]
    strings = [ "aba", "abba", "abaa", "abb"]
    print_Input(infixes, strings)

def print_Input(infixes, strings):
    print("\nRESULTS\n=======")
    for i in infixes:
        print()
        for s in strings:
            print("Infix: %-17s String: %-17s Result: %-5s" % (i, s, thompsonConstruction.NFA.match(i, s)))

userAnswer=True
while userAnswer:
    print("\n1: Print predefined comparisons\n2: Enter infix expressions and strings\n3: Read from file\n4: Exit")
    userAnswer = input("Please enter a option: ")
    # If entry is one print out sample of infix & string comparisions
    if userAnswer == "1":
        infix_Examples()
    elif userAnswer == "2":
        user_input()
    elif userAnswer == "3":
        user_input()
    elif userAnswer == "4":
        print("\nGoodbye") 
        userAnswer = None
    else:
        print("\nNot a valid choice, please try again")