# Treat this file is working as a module where all the required functions are defined
def square(num):
    """This function returns the square of a number"""
    return num ** 2

def cube(num):
    """This function returns the cube of a number"""
    # return num * square(num)
    return num ** 3

def factorial(num):
    """This function returns the factorial of a number"""
    '''
    approach 1
    result = 1 
    for n in range(num, 1, -1):
        result = result * n
    return result
    '''

    '''
    apporoach 2
    if num == 0 or num == 1:
        return 1
    result = 0
    while num > 0:
        result = num * factorial(num - 1)
    retirm result
    '''
    app = int(input("Choose your approach 1 or 2: "))
    if app == 1:
        """This is the iterative approach"""
        result = 1
        for n in range(num, 1, -1):
            result = result * n
        return result
    elif app == 2:
        """This is the base case condition in recursive approach"""
        if num == 0 or num == 1:
            return 1
        return num * factorial(num - 1)

def add(a, b):
    """This function returns the addition of two numbers"""
    return a + b

def subtract(a, b):
    """This function returns the subtraction of two numbers"""
    return a - b

def multiplication(a, b):
    """This function returns the multiplication of two numbers"""
    return a * b

def division(a, b):
    """This function returns the division of two numbers"""
    if a != 0 and b != 0:
        return a / b
    elif a == 0 and b != 0:
        return a / b
    else:
        raise ValueError("You can not divide number with 0") 
    
