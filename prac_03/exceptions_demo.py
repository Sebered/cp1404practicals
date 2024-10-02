"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    When the input is the correct type but an inappropriate value
2. When will a ZeroDivisionError occur?
    When the code tries to divide by 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    Adding a conditional statement to check if the input is zero
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if numerator == 0 or denominator == 0:
        print("Cannot divide by zero >:(")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")