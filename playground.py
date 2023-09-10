import random
numbers = [random.randrange(start=1, stop=17) for _ in range(8)]

a = int(input(f'What is {numbers[1]} X {numbers[2]}'))
b = int(input(f'What is {numbers[2]} X {numbers[2]}'))
c = int(input(f'What is {numbers[3]} X {numbers[2]}'))
d = int(input(f'What is {numbers[1]} X {numbers[2]}'))


if a == a*b:
    a1 = 100