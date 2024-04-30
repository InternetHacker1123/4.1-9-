#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Pair:
    def __init__(self, first, second):
        if not isinstance(first, int) or not isinstance(second, int):
            raise ValueError("Both values should be integers")
        self.first = first
        self.second = second

    def read(self):
        self.first = int(input("Enter the first number: "))
        self.second = int(input("Enter the second number: "))

    def display(self):
        print(f"Pair: ({self.first}, {self.second})")

    def rangecheck(self, num):
        return self.first <= num < self.second


def make_Pair(first, second):
    return Pair(first, second)


if __name__ == "__main__":
    # Пример использования класса Pair
    pair = make_Pair(1, 5)
    pair.display()

    num = int(input("Enter a number to check against the range: "))
    if pair.rangecheck(num):
        print(f"{num} is in the range [{pair.first}, {pair.second})")
    else:
        print(f"{num} is not in the range [{pair.first}, {pair.second})")
