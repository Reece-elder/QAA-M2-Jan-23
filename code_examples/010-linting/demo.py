"""
    Linting / Linter
    Gives you information about how well formatted your code is

    Run a Linter to check our code, it gives us a score and tells us what could be formatted better
    Issues that a linter finds aren't breaking the code, but are just bad practice

    pylint (python based linting tool) pip install pylint (in our terminal)
"""

# from math import sqrt

def printtext():
    """
    A comment about the function
    """
    newvar = 123456
    return f"hello {newvar}"

def standard_statement():
    """
    A comment about the function
    """

    number = 12

    if number >= 20:
        return "number greater than 20"
    return "number less than 20"

print(printtext())
