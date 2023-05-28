import wikipedia

title = input("Search keyword: ")
while title != "":
    try:
        page_title = wikipedia.page(title)
        print(page_title.title)
        print(page_title.summary)
        print(page_title.url)
    except wikipedia.exceptions.DisambiguationError as e:
        print(e.options)
    title = input("Search keyword: ")
