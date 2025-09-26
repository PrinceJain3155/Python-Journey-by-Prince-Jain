#-----------------------------------------------------------------#
# String Functions in Python
#-----------------------------------------------------------------#

"""
  LENGTH OR len() Function
  
  SYNTAX len('name of string or string')

    It tell the length of the string
    it is diffrent from the indexing
    IN indexing it starts from 0 in positive
    BUT
    In len function it do not have positive or negative length
        it counts from 1 like anything normal
        like you have 4 candy you do not count the 0 candy
        if you have n+ ve candy and you cant have -ve number of candy in real life
"""

# Example 1:
a=("Prince Jain") # IN string also count " " as one place in index
print(len(a)) # IN string also count " " as one part of Length of string

#-----------------------------------------------------------------#

"""
    endswith("") Function
    SYNTAX string_name.endswith('the thing user want to check to end with')
      It check weather the give string ends with the given statement or letters
      It output comes in True or False // 1 or 0 respectively (boolean)
"""

# Example 2(a):
b=a #Here i am giving all valuse of a to b 
print(b.endswith("Jain")) #OUTPUT: TRUE
print(b.endswith("  ")) #OUTPUT: FALSE 

# Yes we can even check if the string endswith space or not

#-----------------------------------------------------------------#

"""
    startswith("") Function
    SYNTAX string_name.startswith('the thing user want to check to start with')
      It check weather the give string start with the given statement or letters
      It output comes in True or False // 1 or 0 respectively (boolean)
"""

# Example 2(b):
print(b.startswith("Pri")) #OUTPUT: TRUE
print(b.startswith("  ")) #OUTPUT: FALSE 

# Yes we can even check if the string starts with space or not

#-----------------------------------------------------------------#

#Capatalized
#SYNTAX: string_name.capitalize()
#USED TO capitalize 1st WORD OF STRING
z="prince"
print(z.capitalize()) #OUTPUT: Prince

#-----------------------------------------------------------------#

#Lower
#SYNTAX: string_name.lower()
#USED TO lowers all the WORD OF STRING
x="PRINCE"
print(x.lower()) #OUTPUT: prince

#-----------------------------------------------------------------#

#Upper
#SYNTAX: string_name.upper()
#USED TO captalize all the WORD OF STRING
c="prince"
print(c.upper()) #OUTPUT: PRINCE

#-----------------------------------------------------------------#

#Count letters in one string
#SYNTAX: string.count("c") – counts the total number of occurrences of any character. 
S="abcdacabadbcad"
print(S.count('a')) #OUTPUT: 5

#-----------------------------------------------------------------#

#Finding word in string
"""SYNTAX: string.find(word) - This function finds a word and returns the index of first 
  occurrence of that word in the string. """
string = ('hello world, world is so big i cant imazine to travel the entire world')
print(string.find('world')) #OUTPUT: 6
print(string.find('python')) #OUTPUT: -1 (when not found)

#-----------------------------------------------------------------#

#REPLACING WORDS IN STRING
#string.replace (old word, new word ) – This function replace the old word with 
#new word in the entire string.
string = ('hello world, world is so big i cant imazine to travel the entire world')
print(string.replace('world', "World")) 
# it replace all the occurances of the old word into new word

#-----------------------------------------------------------------#

#STRIP FUNCTION
#SYNTAX: string_name.strip()
#USED TO remove spaces from starting and ending of string
str1="    hello world    "
print(str1.strip()) #OUTPUT: hello world

#-----------------------------------------------------------------#

#SPLIT FUNCTION
#SYNTAX: string_name.split(" ")
#USED TO break the string into list by separator
str2="apple,banana,grapes"
print(str2.split(",")) #OUTPUT: ['apple','banana','grapes']

#-----------------------------------------------------------------#

#JOIN FUNCTION
#SYNTAX: "separator".join(list_name)
#USED TO join list items into one string
list1=['apple','banana','grapes']
print("-".join(list1)) #OUTPUT: apple-banana-grapes

#-----------------------------------------------------------------#

#TITLE FUNCTION
#SYNTAX: string_name.title()
#USED TO capitalize first letter of every word
str3="hello world from python"
print(str3.title()) #OUTPUT: Hello World From Python

#-----------------------------------------------------------------#
