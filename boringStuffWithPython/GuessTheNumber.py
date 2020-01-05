import random


def guesscheck(guess):
    if guess is None:
        print('we will count it anyway...')
        print('You have ' + str(count) + ' more tries')
    elif guess < number:
        print('pick a higher number')
        print('You have ' + str(count) + ' more tries')
    elif guess == number:
        print('Congrats you won!')
    else:
        print('pick a lower number')
        print('You have ' + str(count) + ' more tries')


count = 5
number = random.randint(1, 20)
print(number)
try:
    guess = int(input('guess the number please:'))
except ValueError:
    print('Error: Invalid input')
    guess = None

count = count - 1
guesscheck(guess)

while guess != number:
    try:
        guess = int(input())
    except ValueError:
        print('Error: Invalid input')
        guess = None

    guesscheck(guess)
    if guess == number:
        break

    count = count - 1

    if count == 0:
        print('You Lose! You have no more tries')
        break
