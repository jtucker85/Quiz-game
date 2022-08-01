from qlist import questions
import random

lives = 5
score = 0
qcount = 0

while lives > 0:
    qchoice = random.choices(questions)
    for q,a in qchoice:
        answer = input(f"{q}""?").lower()
        qcount +=1
        if answer == a.lower():
            print("Correct! Well done")
            score +=1
        else:
            lives -=1
            print(f"Sorry! That's incorrect. You have {lives} lives left.")
        


print(f"Oops, you died. You got {score} ({score/qcount*100}%) questions correct.")