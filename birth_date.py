"""
Write a Python 3 program that asks the user how old they are, displays that information back and then informs them how old they will be on their next birthday.
"""

name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

print("Hello {}, you are {} years old. On your next birthday, you will be {} years old.".format(name, age, (age + 1)))

