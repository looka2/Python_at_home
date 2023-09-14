import random
from pprint import pprint


def do_math():
    print("Simple math problems")
    numbers = [random.randint(1, 20) for _ in range(10)]
    answers = []
    grades = []

    for i in range(7):
        operation = random.choice(['*', '-', '+'])
        num1 = numbers[i + 1]
        num2 = numbers[i + 2]
        question = f'What is {num1} {operation} {num2}: '
        answer = int(input(question))
        answers.append(answer)

        if operation == '*':
            correct_answer = num1 * num2
        elif operation == '-':
            correct_answer = num1 - num2
        else:
            correct_answer = num1 + num2

        if answer == correct_answer:
            grade = 100
            print(f'{i + 1}. Correct!')
        else:
            grade = 0
            print(f'{i + 1}. Incorrect')
        grades.append(grade)

    total = sum(grades)
    average = total / 7

    print("\nYour Score is", round(average), "%\n")


if __name__ == '__main__':
    do_math()


def cirkeldiagram():
    import datetime
    datewis1 = datetime.date(2023, 9, 8)

    text = "Gemaakt door Luka op"

    a = (int(input("Wat is het totaal? ")))
    totaal_hoeveelheid = a

    b = (int(input("Wat is de hoeveelheid? ")))
    hoeveelheid_van = b

    # noinspection PyRedundantParentheses
    c = (360 / a) * (b)
    hoeveel_graden = c

    print("\nde hoek is", c, "graden\n")

    print(f'{text}{s}{datewis1}')

    from datetime import datetime

    now = datetime.now()

    dt_n = now.strftime("%Y-%m-%d %H:%M:%S")
    print("Uitgevoerd op", dt_n)


if __name__ == '__main__':
    cirkeldiagram()


def grades():
    print("\nGrading System\n")
    grade = []
    for _ in range(5):
        grade.append(_)
    grade[1] = int(input("Cijfer 1. "))
    grade[2] = int(input("Cijfer 2. "))
    grade[3] = int(input("Cijfer 3. "))
    grade[4] = int(input("Cijfer 4. "))
    avg = round(sum(grade) / 4)
    print("Your score is", avg, "%")


if __name__ == '__main__':
    grades()


def toolbox():
    import pprint
    person = []
    load = int(input("Contact Number Please\n"))

    for _ in range(load + 1):
        person.append(_)
    person[0] = ("Contact Card Bob", "Name : Bob Tutorial", "age : 75", "birthday : Apr 07 1846")
    person[1] = ("Contact Card Jan", "Name : Jan Tutorial", "age : 24", "birthday : jan 14 1999")
    person[2] = ("Contact Card Hola", "Name : Hola Tutorial", "age : 23", "birthday : jan 13 2000")
    person[3] = ("Name = UnLorem")


    person.insert(0, person)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(person[load])


if __name__ == '__main__':
    toolbox()
