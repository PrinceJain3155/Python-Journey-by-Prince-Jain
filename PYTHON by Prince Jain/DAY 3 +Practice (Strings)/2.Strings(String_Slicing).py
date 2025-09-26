#-----------------------------------------------------------------#

# STRING SLICING
"""
    A sting in python can be sliced for getting a part of string
"""

# Consider the following string:

"""

        Name = 'Prince' => Length = 6  "#len(Name)"
    indexing =  012345  => Forward indexing in most of the cases Forward indexing is used
    indexing=-1(654321) => Backward indexing starts from back with index -1 
    
"""
#How to slice a string
name = "Dragon"
sliced = name[0:3] # Start from index 0 all the will till 3 (exculding 3)

print(sliced)

#OR

print(name[:3]) # [:3] if there is nothing in the left side of [:] then it will be considered as 0 in python
#is same as print(name[0:3])

print(name[1:]) # [1:] if there is nothing in the right side of [:] then it will be taken til the last index of the string

print(name[4]) # [4] will only print the character or the valuse of string at 4th index

# for getting the sameoutput we can use negatve indexing though it is not used commonely
print(name[-1])

#another example
print(name[-4:-1])

#Let's try something new
print(name[-1:-4]) #I thought it will print in reversed but it is printing blank space

#Lets try using 3 indexes in range which is also know as  slicing with skip value
num_1="0123456789"
print(num_1[1:7:2])
    # OUTPUT: '135'
    # Here how it works
"""
    First it will run print(num_1[1:7]) """
        #OUTPUT: 123456
"""
    Then it will print valuse starting from start and printevery 2nd number
    Do not get confused it will work like this
        1 (print) 2(skip) 3(print) 4(skip) 5(print) 6(skip)
"""
print(num_1[::2]) # 0(print) 1(skip) 2(print) 3(skip) 4(print) 5(skip) 6(print) 7(skip) 8(print) 9(skip)  

print(num_1[:2:]) 