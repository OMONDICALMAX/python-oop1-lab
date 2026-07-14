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