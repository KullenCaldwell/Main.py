"""'#_Author_ Kullen Caldwell

# Integration Project

# Basic Math Calculator/fun options
"""
''' allows the user to see the menu'''
print("To add numbers together enter 1.")

print("To subtract two numbers enter 2.")

print("To multiply enter 3.")

print("To divide enter 4.")

print("To use exponents enter 5.")

print("To find the remainder of a division problem enter 6.")

print("To do floor division enter 7.")

print("For more fun options enter 8.")

'''takes user input'''

choice = input("Enter your menu choice right here:")

''' adds the first input to the second'''

if choice == '1':

    number1 = float(input("Enter the first number here:"))

    number2 = float(input("Enter the second number here:"))

    print(float(number1 + number2))

    ''' subtracts first input from second'''

elif choice == '2':

    number1 = float(input("Enter the first number here:"))

    number2 = float(input("Enter the second number here:"))

    print(float(number1 - number2))

    ''' multiplies first input by second'''

elif choice == '3':

    number1 = float(input("Enter the first number here:"))

    number2 = float(input("Enter the second number here:"))

    print(float(number1 * number2))

    '''divides first input by second'''

elif choice == '4':

    number1 = float(input("Enter the first number here:"))

    number2 = float(input("Enter the second number here:"))

    print(float(number1 / number2))

    ''' uses the first number as the base and the second as the exponent'''

elif choice == '5':

    number1 = float(input("Enter the first number here:"))

    number2 = float(input("Enter the second number here:"))

    print(float(number1 ** number2))

    ''' finds the remainder of dividing first input by second '''

elif choice == '6':

    number1 = float(input("Enter the first number here:"))

    number2 = float(input("Enter the second number here:"))

    print(float(number1 % number2))

    ''' does floor division of the first and second input'''

elif choice == '7':

    number1 = float(input("Enter the first number here:"))

    number2 = float(input("Enter the second number here:"))

    print(number1 // number2)

    '''gives the user more options if they choose for the fun options'''

elif choice == '8':

    print('multiply a word over as many times as you want enter 1:')

    print('to create a two word sentence enter 2:')

    print('for tax and budget calculator please enter 3:')

    print('To count backwards from a number please enter 4:')

    print('to classify a number enter 6:')

    fun_choice = input("Make choice here:")

    ''' takes user input and multiplies word choice by the number entered'''

    if fun_choice == '1':

        word_choice = input("Enter the word you want to replicate here: ")

        word_mult = int(input("Enter amount of times to replicate here: "))

        fun_choice_1_result = (word_choice * word_mult)

        print(fun_choice_1_result)

        ''' combines the two user inputs to create a two word sentence'''

    elif fun_choice == '2':

        word1 = input("Enter the first word here: ")

        word2 = input("enter the second word here: ")

        print(word1, word2, sep='')

        ''' does a tax calculator based on US tax system'''
    elif fun_choice == '3':
        yearly_income = int(input("Enter your yearly salary:"))
        if yearly_income <= 9875:
            taxes = 9875 * .10
            print("your yearly amount of taxes is:", taxes)
        elif 9875 < yearly_income <= 40125:
            taxes = (yearly_income - 9875) * .12 + 987.50
            print("your yearly amount of taxes is:", taxes)
        elif 40126 < yearly_income <= 85525:
            taxes = (yearly_income - 40125) * .22 + 4617.50
            print("your yearly amount of taxes is:", taxes)
        elif 85525 < yearly_income <= 163300:
            taxes = (yearly_income - 85525) * .24 + 14605.5
            print("your yearly amount of taxes is:", taxes)
        elif 163000 < yearly_income <= 207350:
            taxes = (yearly_income - 163000) * .32 + 33271.5
            print("your yearly amount of taxes is:", taxes)
        elif 207350 < yearly_income <= 518400:
            taxes = (yearly_income - 207350) * .35 + 47367.5
            print("your yearly amount of taxes is:", taxes)
        elif yearly_income > 518400:
            taxes = (yearly_income - 518400) * .37 + 156235.0
            print("your yearly amount of taxes is:", taxes)
        # monthly budget
        monthly_income = (yearly_income - taxes) / 12
        print("your monthly income after taxes is:", monthly_income)
        giving = monthly_income * .10
        print("The amount spent on giving per month:", giving)
        saving = monthly_income * .10
        print("The amount spent on saving per month:", saving)
        food = monthly_income * .10
        print("The amount spent on food per month:", food)
        utilities = monthly_income * .05
        print("The amount spent on utilities per month:", utilities)
        housing = monthly_income * .25
        print("The amount spent on housing per month:", housing)
        transport = monthly_income * .10
        print("The amount spent on transportation per month:", transport)
        health = monthly_income * .05
        print("The amount spent on health a month:", health)
        insurance = monthly_income * .10
        print("The amount spent on insurance a month:", insurance)
        recreation = monthly_income * .05
        print("The amount spent on recreation a month:", recreation)
        personal = monthly_income * .05
        print("The amount spent on personal items a month:", personal)
        misc = monthly_income * .05
        print("The amount spent on miscellaneous a month:", misc)
    # lets the user count down from an integer
    elif fun_choice == '4':
        number_choice = int(
            input("Enter number you want to count down from here:"))
        add_one = (number_choice + 1)
        for (number) in range(0, add_one):
            print(number)
    # determines whether a number is even or add and positive and negative
    elif fun_choice == '5':
        number = int(input("Enter an integer here: "))
        if (number % 2 != 0) and (number > 0):
            print("This number is odd and positive")
        if (number % 2 == 0) and (number > 0):
            print("This number is even and positive")
        if (number % 2 != 0) and (number < 0):
            print("This number is odd and Negative")
        if (number % 2 == 0) and (number < 0):
            print("This number is odd and positive")


else:
    print("Invalid Option have a good day!")

''' or function : 
x = int(input("Enter a number here")
if x < 10 or x > 0
print (" This number is either less than ten or greater than 0")'''
# Function with Docstring
# def author():
#    ''' kullen'''

# author()

# print (author.__doc__)

# While loop Example
'''x = 50
while x >1:
print ("hello world")'''
'''
if ... :
function()'''

'''formatting format(variable,"n.nf")'''
'''end= variable example 
print(Hello!,end= " ")
print("How are you?")'''

# resources that helped me were programmiz found here : \n'
# https://www.youtube.com/watch?v=mrryXQnlYN8&list=PL98qAXLA6afuh50qD\n'
# 2MdAj3ofYjZR_Phn&index=6\n'
# Think python, the Pogils, and the Swebok text\n')

# github link https://github.com/KullenCaldwell/main.py.git
