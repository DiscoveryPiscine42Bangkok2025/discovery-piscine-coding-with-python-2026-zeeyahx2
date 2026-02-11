#!/usr/bin/env python3

year = 10
age = int(input("Please tell me your age: "))
print(f"You are currently {age} years old.")

while year <= 30 :
    print(f"In {year} years, you'll be {age+year} years old.")
    year+= 10