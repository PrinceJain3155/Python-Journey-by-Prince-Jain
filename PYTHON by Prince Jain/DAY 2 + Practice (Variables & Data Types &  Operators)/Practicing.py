# Program 1

# 1. Write a python program to add two numbers.

print("Program 1 : Write a python program to add two numbers.")

a = int(input('ENTER 1st number : ')) 
b = int(input('ENTER 2nd number : '))
print(a+b)
# OR
c = a+b
print(c) 

#-----------------------------------------------------------------#

# Program 2

# 2. Write a python program to find remainder when x number is divided by z

print("Program 2 : Write a python program to find remainder when x number is divided by z")

x =  int(input('ENTER x number : '))
z =  int(input('ENTER z number : '))
remainder = x%z
print(f" remainder when x number is divided by z : {remainder}")

""" f in print function is used to check whether is there any variable in the statement given to print"""

#-----------------------------------------------------------------#

# Program 3

# 3. Check the type of variable assigned using input () function.

print("Program 3 : Check the type of variable assigned using input () function.")

check_type = input("Enter : ")
print(f"The Type or class of {check_type} is ", type(check_type) )

#-----------------------------------------------------------------#

# Program 4

# 4. Use comparison operator to find out whether ‘a’ given variable a is greater than ‘b’ or not. Take a = 34 and b = 80

print("Program 4 : # 4. Use comparison operator to find out whether ‘a1’ is greater than ‘a2’ or not. Take a1 = 34 and a2 = 80 ")

a1 = 34
a2 = 80
print (f"{a1}>{a2}:", a1>a2)
print (f"{a1}<{a2}:", a1<a2)

#-----------------------------------------------------------------#

# Program 5

# 5. Write a python program to find an average of two numbers entered by the user.

print('Program 5 : Write a python program to find an average of two numbers entered by the user.')

_1st = float(input('ENTER 1st number : ')) 
_2nd = float(input('ENTER 2nd number : ')) 

average = (_1st+_2nd)/2
print(f"the average of {_1st} and {_2nd} is {average}")

#-----------------------------------------------------------------#

# Program 6

# 6. Write a python program to calculate the square of a number entered by the user

print('Program 6 : Write a python program to calculate the square of a number entered by the user')

square = float(input('ENTER number : '))
print(f"The square of the number {square} is ", square**2) 

#-----------------------------------------------------------------#