print('-----------------------------')
print('    Guess the Number')
print('-----------------------------')

from random import randint

target = randint(0, 100)
curr = -1

while curr != target:
    curr = int(input('Guess a number between 0 and 100: '))
    if curr == target:
        print(f'YES! You got it. The number was {target}')
        break
    elif curr > target:
        print(f'SORRY but {curr} is HIGHER than the number')
    else: # curr < target
        print(f'SORRY but {curr} is LOWER than the number')