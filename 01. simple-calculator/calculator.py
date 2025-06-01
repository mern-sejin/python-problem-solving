# check input
def isDigit (userInput):
    try:
        float(userInput)
        return True
    except ValueError:
        return False
# calculate function
def calculate (num1, num2, operator):
    match operator:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2
        case _:
            print('Invalid Operator! Please try again.')
            return None
# user input
num1 = input('Number-1: ')
num2 = input('Number-2: ')
operator = input('Operator: ')
# input validation and print result
if isDigit(num1) and isDigit(num2):
    result = calculate(float(num1), float(num2), operator)
    if result != None:
        print('Result is: ', result)
else:
    print('Please enter a valid number!')