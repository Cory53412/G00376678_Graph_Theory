# Author: Cory O'Donoghue
# Graph Theory Project
import shuntingre , thompsonConstruction

def user_Input():
    #user enters their regular expression where it is added to a a list 
    regexInput = input("\nPlease enter your regular expression: ") 
    #user enters string which the want to match to regex
    stringEntry = input("Please enter a string you wish to compare: ")
    #check if user input matches and assign boolean to result
    result = thompsonConstruction.NFA.match(regexInput, stringEntry)

    #if true print this:
    if result:
        print("\nThe regular expression " + regexInput + " matches the string " + stringEntry)
    #else print this:
    else:
        print("\nThe regular expression " + regexInput + " does not match the string " + stringEntry)


def file_Input():
    #user must enter file path
    myInfixFile  = input("\nPlease enter file path of infixes:")
    #opening file
    infix = open(myInfixFile , 'r')
    #taking contents of the file and making them into a list
    i_contents = infix.read().splitlines()
    #print contents of file to screen
    print(i_contents)
    #close file
    infix.close()

    #user must enter file path
    myStringFile  = input("\nPlease enter file path of Strings:")
    #opening file
    strings = open(myStringFile , 'r')
    #taking contents of the file and making them into a list
    s_contents = strings.read().splitlines()
    #printing file contents to screen
    print(s_contents)
    #close file
    infix.close()
    #printing matching strings
    print_Input(i_contents, s_contents)
  

def infix_Examples():
    #array of infixes & strings
    infixes = ["a.b.a**", "a.(b.b)*.a", "a.b.b+"]
    strings = [ "aba", "abba", "abaa", "abb"]

    #loop through infix array
    for i in infixes:
        print()
        #loop through string array
        for s in strings:
            #print i, s and boolean from match function
            print("Infix: %-15s String: %-10s Result: %-5s" % (i, s, thompsonConstruction.NFA.match(i, s)))


userAnswer=True
while userAnswer:
    print("\n1: Print Regular Expressions examples\n2: Enter infix expressions and strings\n3: Read from file\n4: Exit")
    userAnswer = input("Please enter a option: ")
    # If user enters call infix_examples function
    if userAnswer == "1":
        infix_Examples()
    #if user enters two call user input function
    elif userAnswer == "2":
        user_Input()
    #if user enters 3 , call file_input function
    elif userAnswer == "3":
        file_Input()
    #if user selects 4, close the program
    elif userAnswer == "4":
        print("\nClosing program") 
        userAnswer = False
    else:
        print("\nThat was not an option, Please try again")