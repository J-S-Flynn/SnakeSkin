# simple calculator

print('lets get this calculator biult man')

varOne, operator, varTwo = input(' enter your equation ').split()

varOne = int(varOne)

varTwo = int(varTwo)

if operator == '+':
    calc = varOne + varTwo
else:
    if operator == '-':
        calc = varOne - varTwo
    else:
        if operator == '/':
            calc = varOne / varTwo
        else:
            if operator == '*':
                calc = varOne * varTwo
            else:
                if operator == '%':
                    calc = varOne % varTwo

print('the output is {}'.format(calc))

# this also could have used the elif keyword

if calc == 2:
    print("calc is pime")
elif calc % 2 == 0 & calc != 2:
    print("calc is not prime")
elif calc % 2 > 0:
    print('calc might be prime, need to do the loop man.')

