from qlist import questions
import random

lives = 5
score = 0

while lives > 0:
    qchoice = random.choices(questions)
    for q,a in qchoice:
        answer = input(f"{q}""?").lower()
        if answer == a.lower():
            print("Correct! Well done")
            score = score + 1
        else:
            lives = lives - 1
            print(f"Sorry! That's incorrect. You have {lives} lives left.")
        


print(f"Oops, you died. You got {score} questions correct.")