print('How many cats do you own?')
numCats = input()
try:
    if int(numCats) < 0:
        print('Please enter a positive number.')
    else:
        if int(numCats) >= 4:
            print('That is a lot of cats.')
        else:
            print('That is not many cats.')
except ValueError:
    print('Use numeric values.')
