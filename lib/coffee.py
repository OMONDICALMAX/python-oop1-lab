#!/usr/bin/env python3

class Coffee:
    def __init__(self):
        while True:
            self.size = input("Enter size (Small, Medium, or Large): ").capitalize()

            if self.size in ("Small", "Medium", "Large"):
                break

            print("size must be Small, Medium, or Large")

        self.price = float(input("Enter the coffee price: "))

    def tip(self):
        print("This coffee is great, here's a tip!")
        self.price += 1