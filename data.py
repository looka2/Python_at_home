import random


def do_math():
    print("Simple math problems")
    print("1. Mixed Problems")
    """Questions"""
    numbers = [random.randrange(start=1, stop=20) for _ in range(10)]
    a = int(input(f'What is {numbers[1]} X {numbers[5]} : '))
    b = int(input(f'What is {numbers[2]} - {numbers[6]} : '))
    c = int(input(f'What is {numbers[3]} X {numbers[7]} : '))
    d = int(input(f'What is {numbers[4]} + {numbers[8]} : '))

    """Grading system voor toets 1"""

    if a == numbers[1] * numbers[5]:
        a1 = 100
    else:
        a1 = 0
    if b == numbers[2] - numbers[6]:
        b1 = 100
    else:
        b1 = 0
    if c == numbers[3] * numbers[7]:
        c1 = 100
    else:
        c1 = 0
    if d == numbers[4] + numbers[8]:
        d1 = 100
    else:
        d1 = 0

    print("")

    """Answer System"""

    if a == numbers[1] * numbers[5]:
        print("1. Correct!")
    else:
        print("1. Incorrect")
    if b == numbers[2] - numbers[6]:
        print("2. Correct!")
    else:
        print("2. Incorrect")
    if c == numbers[3] * numbers[7]:
        print("3. Correct!")
    else:
        print("3. Incorrect")
    if d == numbers[4] + numbers[8]:
        print("4. Correct!")
    else:
        print("4. Incorrect")

    tot = a1 + b1 + c1 + d1
    avg = tot / 4

    """Grading system voor toets 1"""

    print("Your Score is", avg, "%")


if __name__ == '__main__':
    do_math()


def grades():
    print("")
    print("")
    print("Grading System")


if __name__ == '__main__':
    grades()
