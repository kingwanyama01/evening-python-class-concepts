class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

class Flower:
    def __init__(self, name,price):
        self.name = name
        self.price = price

class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def walk(self):
        return "Yes, I can walk."

    def run(self):
        return "Yes, I can run."


"""
Define a User class with relevant properties.
Ensure the user can register, login and logout.
"""


class User:
    def __init__(self, first_name, last_name, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password

    def register(self):
        return f"I can register with username {self.username} and password {self.password}"

    def login(self):
        return f"I can login with username {self.username} and password {self.password}"

    def logout(self):
        return "I can logout"


class Admin(User):
    pass