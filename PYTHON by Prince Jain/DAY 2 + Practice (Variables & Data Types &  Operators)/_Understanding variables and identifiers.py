# Variable : it stores the given value to memory
# for example it is a container to store somthing and this something is value

#-----------------------------------------------------------------#

# Keyward : reserved words in python
# keywords can never be used as variables as ther are doing seperating things in code

#-----------------------------------------------------------------#

# Identifires : class, function, variable name
# variable is an identifire because it identifies the valuse given by user and it is unique to code

#-----------------------------------------------------------------#

# RULES FOR CHOOSING AN VARIABLE

#  A variable name can contain alphabets, digits, and underscores.
#  A variable name can only start with an alphabet and underscores.
#  A variable name can’t start with a digit.
#  No while space is allowed to be used inside a variable name.

# Examples; seven, _seven, SEVEN7

#-----------------------------------------------------------------#

'''

# DATA TYPES

Primarily these are the following data types in Python:
    1. Integers
    2. Floating point numbers
    3. Strings
    4. Booleans
    5. None

Python automatically identifies the type of data for us

'''

#-----------------------------------------------------------------#

integer = 3155 # identifies it as class <int>
    # In python numbers are refered as integer in short int
decimal = 0.001 # identifies it as class <float>  
    # In python decimal numbers are takens as float data type
string = 'Prince' # identifies it as class <str> 
    # In python words are reffred as string in short str

'''
NOTE: anything in '' or "" even it is number is reggred as string in python

'''

#-----------------------------------------------------------------#

print("TYPE() FUNCTION")

a = 31
type(a) # class int
print("type of a is:", type(a))

b = "31"
type(b) # class str
print("type of b is:", type(b))

#-----------------------------------------------------------------#

print("TYPECASTING")
# taking data of a and b from previous block

a_str = str(a)
print(a_str, type(a_str))
a_int = int(a)
print(a_int, type(a_int))
a_float = float(a)
print(a_float, type(a_float))

#-----------------------------------------------------------------#

print("INPUT() FUNCTION")

# input function is used to take input from user

A = input("now user can feed or input the value needed buy code: ")
#input always gives data type as string to the value given by user

#-----------------------------------------------------------------#

"""

OPERATORS IN PYTHON

    Following are some common operators in python:

        1. Arithmetic operators: +, -, *, / etc.
        2. Assignment operators: =, +=, -= etc.
        3. Comparison operators: ==, >, >=, <, != etc.
        4. Logical operators: and, or, not.

"""

#-----------------------------------------------------------------#