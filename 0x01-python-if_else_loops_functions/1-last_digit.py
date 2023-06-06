#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last_digit = number % 10
else:
    last_digit = -1 * (abs(number) % 10)
const = f"Last digit of {number:d} is {last_digit:d}"
if last_digit == 0:
    print(const + " and is 0")
elif last_digit > 5:
    print(const + " and is greater than 5")
else:
    print(const + " and is less than 6 and not 0")
