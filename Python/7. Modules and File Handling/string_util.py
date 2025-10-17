# reversal of string:
def reverse(str):
    """This function gives the reverse string"""
    return str[::-1]

def is_palindrome(str):
    """This function gives the result where string is palindrome or not"""
    if str == str[::-1]:
        return True
    else:
        return False
    
def concatinate(str1, str2):
    """This function concatinates the two given strings"""
    return str1 + str2

def string_length(str):
    """This function gives the length of string"""
    return len(str)

