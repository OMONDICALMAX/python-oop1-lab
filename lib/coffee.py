#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price
    
    while True:
        size = input("Enter size(small, medium, or large): ").lower()
        if size in ("small", "medium", "large"):
            break
        else: 
            print("Size must be Small, Medium, or Large")
    print(f"You selected: {size}")

    while True:
        try:
           price = int(input("Enter coffee price: "))
           break
        except ValueError:
           print("Coffee price must be in numbers!")
    
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1
    def display(self):
        print(f"Size: {self.size}")
        print(f"Price: {self.price}")
    
coffee1 = Coffee("small", 50)

coffee1.tip()
coffee1.display()