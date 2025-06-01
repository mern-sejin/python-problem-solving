# main function
def check (number):
    num = int(number)
    if num % 2 == 0:
        print(f'{num} is an even number.')
    else:
        print(f'{num} is an odd number.')
# user input
number = input('Number: ')
try:
    num = int(number)
    check(num)
except ValueError:
    print('Please enter a valid integer!')