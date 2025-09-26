#Program 1

# 1. Write a python program to display a user entered name followed by Good  Afternoon using input () function.

print("Program 1 : Write a python program to display a user entered name followed by Good  Afternoon using input () function.")

name=input("Enter your name:")
print(f"Good Afternoon {name}")

#-----------------------------------------------------------------#

# Program 2

# Write a program to fill in a letter template given below with name and date. 
"""letter = '''  
    Dear <|Name|>, 
    You are selected! 
    <|Date|> 
    ''' """

print("Program 2 : Write a program to fill in a letter template given with name and date.")
print(f"""letter = '''  
    Dear <|Name|>, 
    You are selected! 
    <|Date|> 
    '''\n After replacing we get: """)

letter = """Dear <|Name|>, 
You are selected! 
<|Date|> 
"""

print(letter.replace("<|Name|>", "Prince Jain").replace("<|Date|>", "28 September 2025"))

#-----------------------------------------------------------------#

# Program 3

# 3. Write a program to detect double space in a string.

print("Program 3 : Write a program to detect double space in a string.")

string="Prince Jain is a good  boy"
b = string.find("  ")
print(string)
print(f"Double space is dected at {b} index")

#-----------------------------------------------------------------#

# Program 4

# 4. Replace the double space from problem 3 with single spaces. 

print("Program 4. Replace the double space from problem 3 with single spaces. ")
string="Prince Jain is a good  boy"
b = string.replace("  ", " ")
print(string)
print(f"new string formed after replacing the double space with single space \n {b}")

#-----------------------------------------------------------------#

# Program 5

# 5. Write a program to format the following letter using escape sequence 
    #characters. 
        #letter = "Dear Harry, this python course is nice. Thanks!" 

print(""""Program 5. Write a program to format the following letter using escape sequence  characters. 
letter = "Dear Prince Jain, this python course is nice. Thanks!" """)
letter = "Dear Prince Jain, this python course is nice. Thanks!"
print("Dear Prince Jain,\nThis python course is nice.\nThanks!")

#-----------------------------------------------------------------#
