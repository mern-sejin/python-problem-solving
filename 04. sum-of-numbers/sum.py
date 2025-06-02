number = input('Number: ')
if number.isdigit():
    # using formula
    number = int(number)
    sum1 = (number * (number + 1)) / 2
    print('Using Formula:', int(sum1))

    # using for loop
    sum2 = 0
    for i in range (1, number + 1):
        sum2 += i
    print('Using For Loop:', int(sum2))

    # using while loop
    i = 1
    sum3 = 0
    while i <= number:
        sum3 += i
        i += 1
    print('Using While Loop:', int(sum3))
else:
    print('Please enter a positive integer number!')