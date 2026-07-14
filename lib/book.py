class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count


title = input("What is the title of the book you want to read today? ")

while True:
    try:
        page_count = int(input("What page do you want to jump to? "))
        break
    except ValueError:
        print("Page count must be an integer!")

book1 = Book(title, page_count)

print(book1.title)
print(book1.page_count)