"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random

def main():
        score = float(input("Enter score: "))
        result = calculate_result(score)
        print(result)

        random_score = random.randint(0, 100)
        random_result = calculate_result(random_score)
        print(random_result)
        

def calculate_result(score):
    if 0 < score <= 100:
        if score < 50:
            result = "Bad"
        elif score < 90:
            result = "Passable"
        else:
            result = "Excellent"
    else:
        result = "Invalid score"
    return result

main()