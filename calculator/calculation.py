print('\nA basic calculator based on Python, start providing a calculation below:')
import time
import math


def get_float_input(prompt):
    # Provides a backup for any empty input, also makes sure that the console doesnt automatically fail a loop upon startup because of no value provided
    while True:
        data = input(prompt).strip()
        if not data:
            print("\nWait, you havent typed anything? How do you calculate then?")
            continue
        return float(data)



def calculation():
    num1 = get_float_input('Enter the first number: ')

        # LIST OF OPERATION SYMBOLS
    print('''
        -- SYMBOLS TO USE

        Make sure you use the actual symbol and not the name.
          
        / = Division
        + = Addition
        - = Subtraction
        * = Multiplication
        num% = Percentage
        ** = Exponentation
        // = Floor Division
        % = Modulo
        sq = Squaring (SINGLE-NUMBER)
        sqrt = Square Root (SINGLE-NUMBER)
        graph = Graphing (SINGLE-NUMBER)''')
    time.sleep(1)
    symbol = input('Enter a symbol: ').strip()



    # SINGLE NUMBER OPERATIONS

    if symbol == 'sq':
        return f'Squaring {num1} gives the result of: {num1 ** 2}.'
    
    if symbol == 'sqrt':
        if num1 < 0:
            return 'Cannot calculate the square root of a negative number in real numbers.'
        
        return f'The square root of {num1} is.. {num1 ** 0.5}.'

    if symbol == 'graph':
        limit = int(num1)
        output = f"\nGraph for y = x^2 (x from 0 to {limit}):\n"
        for i in range(limit + 1):
            output += f"x={i}: " + ('■' * (i**2)) + "\n"
        return output
    


    # DOUBLE NUMBER OPERATIONS

    num2 = get_float_input('Enter the second number: ')

    # Conditions of symbols

    if symbol == '/':
        if num2 == 0:
            return 'Division by zero is not defined. Try with something else'
        else:
            return f'Dividing {num1} by {num2} equals to.. {num1 / num2}. '

    if symbol == '//':
        if num2 == 0:
            return 'Floor division by zero is not defined. Try with something else'
        else:
            return f'Floor dividing {num1} by {num2} equals to.. {num1 // num2}. '

    if symbol == '+':
        return f'Adding {num2} to {num1} equals to.. {num1 + num2}.'

    if symbol == '-':
        return f'Removing {num2} from {num1} has the remainder of: {num1 - num2}'

    if symbol == '**':
        if num2 > 500:
            raise OverflowError('num2 has been requested to modify num1 but the result is way too large for processing. Please try again')
        else:
            return f'{num1} to the power of {num2} is... {num1 ** num2}'
    
    if symbol == '%':
        if num2 == 0:
            return 'Modulo by zero is not defined.'
        else:
            return f'The remainder of {num1} divided by {num2} is... {num1 % num2}'
    
    if symbol == 'num%':
        return f'{num2}% percent of {num1} is.. {num1 / 100 * num2}'
    
    if symbol == '*':
        return f'{num1} multipled by {num2} results in.... {num1 * num2}'

    else:
        return('Invalid symbol has been provided, please try again with the right one')
    

while True:
    try:
        print("\n--- Proccessing a new calculation. ---")
        print(calculation())
    except ValueError:
        print('Oops!, It looks like you have inserted in a invalid number/value. Make sure its only a number!')