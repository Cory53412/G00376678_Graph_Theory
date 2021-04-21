## G00376678_Graph_Theory
An application written in python3 to search a text file using a regular expression. This program takes a regular expression and the name or path of the file as command line arguments and output the lines of the file matching the regular expression.

## Instructions
To run the application:
* Have python installed and set up on your machine 
* Clone the repo to your machine - git clone https://github.com/Cory53412/G00376678_Graph_Theory
* cd into G00376678_Graph_Theory
* Have a script editor like Visual Studio code
* Run application from cmd using command 'python menu.py'

## Explanation of the algorithem
#### Converting infix to postifx using Shunting Yard algorithem (shunt function)
To convert an infix expression into a postfix expression we use a stack to hold the operators and reverse their order in the expression. All the operands are printed when they are read. Below are the rules to handle operators and parantheses which you can find here along with examples from 
[The Departments of Mathematics and Computer Science](http://mathcenter.oxford.emory.edu/site/cs171/shuntingYardAlgorithm/).
* If the incoming symbols is an operand, print it..
* If the incoming symbol is a left parenthesis, push it on the stack.
* If the incoming symbol is a right parenthesis: discard the right parenthesis, pop and print the stack symbols until you see a left parenthesis. Pop the left parenthesis and discard it.
* If the incoming symbol is an operator and the stack is empty or contains a left parenthesis on top, push the incoming operator onto the stack.
* If the incoming symbol is an operator and has either higher precedence than the operator on the top of the stack, or has the same precedence as the operator on the top of the stack and is right associative -- push it on the stack.
* If the incoming symbol is an operator and has either lower precedence than the operator on the top of the stack, or has the same precedence as the operator on the top of the stack and is left associative -- continue to pop the stack until this is not true. Then, push the incoming operator.
* At the end of the expression, pop and print all operators on the stack. (No parentheses should remain.)
[Add image below]


#### Creating an NFA using Thompsons Construction Algorithem (re_to_nfa function)
Once the shunting yard algorithem has created the postfix notation, we use an alogrithem called thompsons construction which iterates through the postfix expression. It checks for each operator (* + . |) and creates a small NFA to add to the overall stack. These work by setting up inital and accept states using NFA class and constructor. I discuss how these operators work briefly further down.
[Add image below]


#### Match() function
This function converts the infix expression into a postfix and checks if the regular expression matches the given string of text. It gets the postfix by calling re_to_nfa(). It then creates a current set of states and a previous set of states. Afterwards looping through the states and follows e arrows of the curent state.
This is implemented using the followes function which is talked about below. For each character in the string iterate through the current set to check if the set contains the character, if so, add the next states you could travel to. At the end if the current set contains the accept state then it returns true, if not then returns false and the string doesn’t match the NFA.
[Add image below]

#### followes() function
This function takes in the current state and the state to be checked. It ensures both edges are followed

## UI Functions
#### Infix_Examples()
This function displays a list of previosuly tested regular expressions and their matching strings.

#### User_Input()
This function asks the user to enter a regular expression, once theyve enter their regex then the program asks the user to enter a string. The function will then return a message to the user telling stating if the two entires match or not.

#### File_Input()
This function asks the user to enter a directory of a file they wish to read consisting of infix values, the user will then be asked to repeat the previous task but enter a file directory for strings.

## What is a regular expression?
Regular expression originated in 1951, a mathematition Stephen Cole Kleene described regular languages using his mathematical notation called regular events. A regular expression which can be shortened to regex is a string of text that allows you to create patterns that help match, locate, and manage text. These strings are compared to this pattern to see if they fit the pattern defined by the expression. Regex is a combination of two types of characters, literals and special characters. These charcters define the logical pattern. Literals are all charcters except those with special meanings. In total there are twelve charcters with special meanings. These are '\' , '^', '$' , '.' , '|' , '?' , '*' , '+' , '(' , ')' '{' '[]' 

Special character meanings:
* \-Backslash escape charcter
* ^-Carpet is the anchor for start of the string
* $-The dollar sign is the anchor for the end of the string
* .-The dot matches any charcter except newline symbol 
* |-Seperates a series of alternatives
* ?-Question mark is the match one or more quantifier
* *-Asterisk is the match zero or more quantifier
* +-Plus is the match one or more quantifier
* <>- Smaller and greater signs are anchors that specify a left or right word boundary
* ()-Opening and closing parentheses are used for grouping characters.
* {}-Opening and closing curly brackets are used as range quantifiers
* []-Opening and closing square brackets define a character class to match a single character

If you were to match a character having special meaning you need to use an escape sequence prefix with a backslash E.g \. matches "." or \+ matches "+".

Regular Expressions consist of constraints, which denote sets of strings and operator symbols that denote operations over these sets. Given a finite alphabet Σ, the following constants are defined as regular expressions:

* Empty set-∅ denoting the set ∅.
* Empty string- ε denoting the set containing only the "empty" string, which has no characters at all
* Literal character -  ε denoting the set containing only the "empty" string, which has no characters at all
* Kleene star - R* denotes the smallest superset of the set described by R that contains ε and is closed under string concatenation.
* Concatenation-(RS) denotes the set of strings that can be obtained by concatenating a string accepted by R and a string accepted by S.
* Alternation-(R|S) denotes the set union of sets described by R and S.


## how do regular expressions differ across implementations?

## Can all formal languages be encoded as regular expressions?
