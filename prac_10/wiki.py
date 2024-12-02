import wikipedia

user_input = input("Wikipedia search query: ")

while user_input != "":
    try:
        article = wikipedia.page(user_input)
        print(article.title)
        print(article.summary)
        print(article.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(e.options)
    except wikipedia.exceptions.PageError:
        print(f'Page id "{user_input}" does not match any pages. Try another id!')
    print("")
    user_input = input("Wikipedia search query: ")
print("Thank you!")