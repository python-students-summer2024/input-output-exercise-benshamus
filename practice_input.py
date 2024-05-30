"""
A little assignment to practice receiving text input from the user in Python programming.
Do not run this file... run main.py instead.
"""


def get_favorite_vegetable():
    """
    Asks the user to enter their favorite vegetable
    and then prints out, "Interesting! I also love X!",
    where X is replaced with the user's favorite vegetable.
    """
    # write your code here.
    vegetable = input("What is your favorite vegtable?")
    print(f"Interesting! I also love {vegetable}!")


def get_favorite_number():
    """
    Asks the user to enter their favorite number
    and then prints out, "Interesting! I also love X!",
    where X is replaced with the user's favorite number.
    """
    # write your code here.
    number = input("What is your favorite number?")
    print(f"Interesting! I also love {number}!")


def get_name_and_zodiac_sign():
    """
    Asks the user to enter their name.
    Then ask them to enter their zodiac sign.
    Then print out, "Interesting! My name is also X, and I'm also a Y!",
    where X and Y are replaced by the user's name and zodiac sign, respectively.
    """
    # write your code here.
    my_name = input("What is your name?")
    my_zodiac = input("What is your zodiac sign?")
    print(f"Interesting! My name is also {my_name}, and I'm also a {my_zodiac}!")


def get_name_and_age():
    """
    Asks the user to enter their name.
    Then ask them to enter their age.
    Then print out, "Interesting! My name is also X, and I'm also Y years old!",
    where X and Y are replaced by the user's name and age, respectively.
    """
    # write your code here.
    my_name = input("What is your name?")
    my_age = input("What is your age?")
    print(f"Interesting! My name is also {my_name}, and I'm also {my_age} years old!")