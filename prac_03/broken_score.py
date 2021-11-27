from random import random


def main():
    score = float(input("Please enter your score: "))
    level(score)


def level(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 85:
        print("Excellent,you got HD")
    elif score >= 75:
        print("Very nice,you got D")
    elif score >= 65:
        print("Good,you got C")
    elif score >= 50:
        print("Pass,keep it up,you got P")
    else:
        print("Bad,You need to study hard,you got F")


main()

import random

print(random.randint(0, 100))
