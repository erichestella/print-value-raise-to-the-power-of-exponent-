#added some title
print('\nDISPLAYING THE TOTAL NUMBER THAT IS RAISED TO THE POWER.\n')

#variables to input the number and the power
numerical_digit = int(input('ENTER NUMBER: '))
exponential_integers = int(input('\nINPUT THE POWER: '))

#it display the number you just input
numerical_define = str(numerical_digit)

#this function multiply the numerical digit you just input and the exponential integers
for n in numerical_define:
    total= int (n) ** exponential_integers

#it display the total of numerical digit and exponential integers y0u multiply 
print('\nTOTAL INTEGERS: ',total, '\n')