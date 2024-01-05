#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
lastDigit = 0

if num >= 0:
    lastDigit = num % 10
else:
    lastDigit = (-num % 10) * -1

message = f"Last digit of {number} is {lastDigit}"

if lastDigit == 0:
    print(f"{message} and is 0")
elif lastDigit > 5 and lastDigit % 10 != 0:
    print(f"{message} and is greater than 5")
else:
    print(f"{message} and is less than 6 and not 0")
