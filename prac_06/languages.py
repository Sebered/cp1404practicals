from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)


def main():
    languages = [python, ruby, visual_basic]
    print(python)

    print("The dynamically typed languages.csv are: ")
    for item in languages:
        if item.typing == "Dynamic":
            print(item.name)


main()