import random


def random_formula():
    '''
    Generate a random formula.
    '''
    # List of operators
    operators = ['+', '-', '*', '/']
    # List of numbers
    numbers = [str(i) for i in range(10)]
    # List of variables
    variables = ['x', 'y', 'z']
    # List of functions
    functions = ['sin', 'cos', 'tan', 'log', 'exp']
    # List of brackets
    brackets = ['(', ')']
    # List of all possible characters
    characters = operators + numbers + variables + functions + brackets
    # Number of characters in the formula
    length = random.randint(5, 10)
    # Generate the formula
    formula = ''.join(random.choices(characters, k=length))
    # Return the formula
    return formula

if __name__ == '__main__':
    # Print a random formula
    print(random_formula())