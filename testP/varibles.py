# Python takes all vars as a string i=unless spacifiv=caly asked no to i.e

myVar = input('Give me a intiger please : ')

print('The content of myVar is : ', myVar)

myVar = input('Now give me a string : ')

print('Now the content of myVar is : ', myVar)

print('\n\nthe content of variables in python are all string se we need to convert to int .')

varOne = input('give me a number : ')
varTwo = input('give me  another : ')

# to get two things we could do this in one line as varOne, varTwo = input('Enter two number : ').split()
# dont belive me, go ahead and try it


# change the strings to int
varOne = int(varOne)
varTwo = int(varTwo)

# addition
addition = varOne + varTwo

print('vOne + vTwo = ', addition)

# subtraction
subtraction = varOne - varTwo

print('vOne - vTwo = ', subtraction)

# multiplacation
product = varOne * varTwo

print('vOne * vTwo = ', product)

# division
quationt = varOne / varTwo

print('vOne / vTwo = ', quationt)

# modules
remainder = varOne % varTwo

print('vOne % vTwo = ', remainder)


print('or all together we have ')
print("{} + {} = {}".format(varOne, varTwo, addition))

