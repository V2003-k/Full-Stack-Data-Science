import calculator as calc

# fact_reslut = calc.factorial(11)
# square_result = calc.square(11)
# cube_result = calc.cube(11)
# print(f"The factorial of 11 is: {fact_reslut}")
# print(f"The square of 11 is: {square_result}")
# print(f"The cube of 11 is: {cube_result}")

# import string_util as str

# reverse_string = str.reverse("Hello")
# print(f"The reverse of 'Hello' as {reverse_string}")

# palindrome_check = str.is_palindrome("madam")
# print(f"Is 'madam' a palindrome ?: {palindrome_check}")

# from string_util import concatinate

# s1 = "hello"
# s2 = "world"
# print(f"Concatinated String: {concatinate(s1, s2)}")

import math 
x = min(1, 2, 3, 4, 5, 0, -1)
# print(x)
print(f"Square root of {16} is: {math.sqrt(16)}")
print(math.ceil(4.2))
print(abs(-4.2))
print(math.factorial(5))
print(math.pi)

import datetime
today = datetime.date.today()
print(f"Todays date is: {today}")

now = datetime.datetime.now()
print(f"Timestamp: {now}")

import random

randum_number = random.randint(1, 100)
print(f"Random Number: {randum_number}")
print(random.choice(['apple', 'banana', 'cherry']))