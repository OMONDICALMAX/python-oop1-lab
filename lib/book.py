#!/usr/bin/env python3
class Book:
    def __init__(self):
        self.title = input("Enter the book title: ")

        while True:
            try:
                self.page_count = int(input("Enter the page count: "))
                break
            except ValueError:
                print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")