#-----------------------------------------------------------------#
'''
STRINGS:
Strings are data types in python
String is immutable Data type
Sting is sequence of characters enclosed in quotes
String is an ordered data type : meaning we can use indexing to get the value

'''
#-----------------------------------------------------------------#

name = "Prince Jain" #This is an string
section = 'C' #This is an string
programing_languages = '''Python, 
Java,
C++,
Html, CSS
''' #multiline String
print(name)
print(section)
print(programing_languages) 

#-----------------------------------------------------------------#

#AS string is a data type in python we can use TYPE() function to know if out stored value in variables are string class or not
print(type(name))
print(type(section))
print(type(programing_languages))

#-----------------------------------------------------------------#

#WE can make string using str() function or change its datatype
a = float(input("ENTER NUMBER:"))
print(f"Data type of {a} before using str() is:", type(a))
print(f'After using str() function data type of {a} is:', type(str(a)))

#-----------------------------------------------------------------#