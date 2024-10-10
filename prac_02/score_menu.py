MENU = """
    (G)et a valid score (must be 0-100 inclusive)
    (P)rint result (copy or import your function to determine the result from score.py)
    (S)how stars (this should print as many stars as the score)
    (Q)uit
"""

def main():
    score = get_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_score()
        elif choice == "P":
            result = calculate_result(score)
            print(result)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Goodbye.")

def get_score():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Score is invalid.")
        score = float(input("Enter score: "))
    return score

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

def show_stars(score):
    for i in range(int(score)):
        print("*", end="")
    print("")


main()