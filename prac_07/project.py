
MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit
>>> """

def main():
    user_input = input(MENU).upper()
    while user_input != "Q":
        if user_input == "L":
            print("Load projects")
        elif user_input == "S":
            print("Save projects")
        elif user_input == "D":
            print("Display projects")
        elif user_input == "D":
            print("Filter projects by date")
        elif user_input == "A":
            print("Add new project")
        elif user_input == "U":
            print("Update project")
        else:
            print("invalid")

        user_input = input(MENU).upper()

    print("Quit")


main()