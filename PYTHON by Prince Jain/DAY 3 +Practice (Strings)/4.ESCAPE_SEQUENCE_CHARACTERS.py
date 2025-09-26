#-----------------------------------------------------------------#
# ESCAPE SEQUENCE CHARACTERS
#-----------------------------------------------------------------#

"""
Sequence of characters after backslash "\" → Escape Sequence characters 

Escape Sequence characters are written with a "\" (backslash) before them.  
They look like 2 characters but when used in string they represent only 1 character.  

For Example: 
    "\n" is written as 2 characters but represents just a single "new line".  
"""

#-----------------------------------------------------------------#

# NEW LINE → \n
print("Hello\nWorld")
# OUTPUT:
# Hello
# World

#-----------------------------------------------------------------#

# TAB SPACE → \t
print("Hello\tWorld")
# OUTPUT: Hello    World   (adds a tab space)

#-----------------------------------------------------------------#

# SINGLE QUOTE → \'
print('It\'s a sunny day')
# OUTPUT: It's a sunny day

#-----------------------------------------------------------------#

# DOUBLE QUOTE → \"
print("He said \"Python is easy\"")
# OUTPUT: He said "Python is easy"

#-----------------------------------------------------------------#

# BACKSLASH → \\
print("This is a backslash: \\")
# OUTPUT: This is a backslash: \

#-----------------------------------------------------------------#

# BACKSPACE → \b
print("Hello\bWorld")
# OUTPUT: HellWorld  (removes the 'o')

#-----------------------------------------------------------------#

# CARRIAGE RETURN → \r
print("Hello\rWorld")
# OUTPUT: World  (cursor moves to start, so "World" overwrites "Hello")

#-----------------------------------------------------------------#
