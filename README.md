## Simple calculator proyect

## BEFORE I EXPLAIN THE CODE
Thank you for viewing my first Python proyect! It means a lot to me and i might build a portafolio of different programming languages. Have a great day and you may continue ;)
As i advance in coding, i may take more time to code stuff, but ill make huge proyects which will be completely functional!



# EXPLANATION

This is a calculator you can use in the console. It is written in Python as part of my learning journey and is really easy to use
## Features

* You can do a calculation for math numbers: It supports 7 double-number operators and 3 single-number operators.
* The calculator checks your input carefully, so it won’t get confused if you enter something nonsensical.
* It also helps prevent mistakes, in any type, such as dividing by zero



Download the calculator.py file.
Open the terminal or command prompt, navigate to the folder, and run the script:

python calculator.py

## How to Use

The calculator will keep running until you stop it, (CTRL + C on keyboard to manually stop the entire code) here’s what you need to do:

1. Enter your first number (affected/modified number)
2. Look at the list of symbols and type the one you want to use
3. If your operation requires two numbers, enter the second number (number that will modify the other)

## Supported Symbols

* / means divide

* + means add

* - means subtract

* * means multiply

* % means percentage

* ** means exponent

* // means divide and take the integer part

* % means find the remainder

* sq means square a number

* sqrt means find the root

* graph means create a graph of y = x^2

   # else, the file already has a list, though wont be updated anymore

## What's in the code?

get_float_input is a function that retrieves a number from the user. It ensures there are no spaces and prompts again if the user enters nothing.
calculation is the function that performs the math. It checks what the user wants to do and returns the answer.
The calculator uses try-except blocks to handle mistakes and keep running.
