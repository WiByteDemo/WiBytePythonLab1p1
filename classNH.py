import random
n = random.randint(1, 100)

print('I picked a number between 1 and 100, can you guess?')

done = True
attempts = 0

while not done:
    guess = int(input('Guess the number\n'))
    attempts = attempts + 1

    if guess > n:
        print('My number is smaller than that.\n')

    if guess < n: 
        print('My number is larger than that.\n')

    if guess == n:
        print('Bingo, correct')
        print('Attempts taken', attempts)
        done = True

# Computer Guessing
print()
print()
print('Now your chance, pick a number between 1 and 100')
print('Click enter when ready')

input()
done = False
guess = 1
attempts = 0

guess_step = 10
#prev_answer = ''

while not done: 
    answer = input('Is it ' + str(guess) + '? (y = yes, s = smaller than that, l = larger than that)')
    attempts = attempts + 1

    if attempts > 1:
        if answer != prev_answer:
            guess_step = guess_step - 1

    prev_answer = answer


    if answer == 's':
        guess = guess - guess_step

    if answer == 'l':
        guess = guess + guess_step

    if answer == 'y':
        print('Bingo, got it')
        print('attempts taken', attempts)
        done = True
