import random
def do_math():
    print("Some simple math problems")
    print("Toets 1")
    """Questions"""
    aa = random.randrange(start=1, stop=17)
    ab = random.randrange(start=1, stop=17)
    ba = random.randrange(start=600, stop=800)
    bb = random.randrange(start=60, stop=600)
    ca = random.randrange(start=70, stop=97)
    cb = random.randrange(start=1, stop=97)
    da = random.randrange(start=30, stop=87)
    db = random.randrange(start=1, stop=9)
    a = int(input(f'What is {aa} X {ab}: '))
    b = int(input(f'What is {ba} - {bb}: '))
    c = int(input(f'What is {ca} + {cb}: '))
    d = int(input(f'What is {da} ÷ {db}: '))

    """Grading system voor toets 1"""

    if a == aa*ab:
        a1 = 100

    else:
        a1 = 0

    if b == ba-bb:
        b1 = 100

    else:
        b1 = 0

    if c == ca+cb:
        c1 = 100

    else:
        c1 = 0

    if d == da/db:
        d1 = 100

    else:
        d1 = 0

    print("")

    """Answer System"""

    if a == aa*ab:
        print("1. Correct!")

    else:
        print("1. Incorrect")

    if b == ba-bb:
        print("2. Correct!")

    else:
        print("2. Incorrect")

    if c == ca+cb:
        print("3. Correct!")

    else:
        print("3. Incorrect")

    if d == da/db:
        print("4. Correct!")

    else:
        print("4. Incorrect")

    tot = a1 + b1 + c1 + d1
    avg = tot / 4



    """Grading system voor toets 1"""

    print("Your Score is",(avg),("%"))


if __name__ == '__main__':
    do_math()


def grades():
    print("")
    print("")
    print("Grading System")


if __name__ == '__main__':
    grades()
