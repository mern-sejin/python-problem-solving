userInput = input('Write a letter: ')
vowels = ['a', 'e', 'i', 'o', 'u']
if not userInput.isalpha() or len(userInput) > 1:
    print('Please enter a single alphabet letter!')  
elif userInput.lower() in vowels:
    print(f'`{userInput}` is a vowel.')
else:
    print(f'`{userInput}` is a consonant.')