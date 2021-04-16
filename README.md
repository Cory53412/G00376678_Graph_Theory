## G00376678_Graph_Theory
An application written in python3 to search a text file using a regular expression. This program takes a regular expression and the name or path of the file as command line arguments and output the lines of the file matching the regular expression

## Instructions
To run the application:
* Have python installed and set up on your machine 
* Clone the repo to your machine - git clone https://github.com/Cory53412/G00376678_Graph_Theory
* cd G00376678_Graph_Theory
* Have a script editor like Visual Studio code
* Run application from cmd using command 'python regex.py'

## Explanation of the algorithem

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
* ()-Opening and closing parentheses are used for grouping characters.
* {}-Opening and closing curly brackets are used as range quantifiers
* []-Opening and closing square brackets define a character class to match a single character

If you were to match a character having special meaning you need to use an escape sequence prefix with a backslash E.g \. matches "." or \+ matches "+".





* <>- Smaller and greater signs are anchors that specify a left or right word boundary


## how do regukar expressions differ across implementations?

## Can all formal languages be encoded as regular expressions?
