import random
import sys

# function that check if the input given by the user is numeric
def isInt(toCheck):

    if not toCheck.isnumeric():
        sys.exit('You can only input numbers')

# variable that stores a ranodm number between 1 and 100 that the
# user has to guess
randomInt = random.randint(1, 100)

print(randomInt, 'Is the number you have to guess.')

# promps the user to guess the number
userGuess = input('Guess the number! please insert a number to start. ')

# check if the input given by the user is numeric
isInt(userGuess)

# assigns the varible as a int class
userGuess = int(userGuess)

# initializing the variable for the while loop
answer = False

# initializing the variable that will store the number
# of attempts the user will make
totalAttempts = 0

# we will loop till the variable answer is change to True.
# isClose variable stores the random generated number the
# user has to guess and subtracts the userGuess
# if the user guess is plus or minus 10 points away 
# it will print Close, else it will print Keep trying
while answer == False:
    
    isClose = abs(randomInt - userGuess)

    if userGuess == randomInt:
        print('Correct')
        answer = True
    elif isClose <=  10:
        print('Close\n')
        userGuess = input('Please insert a number to try again ')
        isInt(userGuess)
        userGuess = int(userGuess)
    else:
        print('Keep trying\n')
        userGuess = input('Please insert a number to try again ')
        isInt(userGuess)
        userGuess = int(userGuess)
    
    # every time the loop complets one loop increase
    # the totalAttempts variable by one
    totalAttempts += 1

# print the users total attemtpts to guess the number
print('Total number of attempts', totalAttempts)