import random

number_of_picks = int(input("How many quick picks? "))

for i in range(number_of_picks):
    quick_picks = []
    for j in range(6):
        number = random.randint(1, 45)
        while number in quick_picks:
            number = random.randint(1, 45)
        quick_picks.append(number)
    quick_picks.sort()
    print(" ".join(f"{number:2}" for number in quick_picks))

