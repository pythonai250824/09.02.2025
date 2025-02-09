import math
import sqlite3

def add(a, b):
    return a + b  # + 0.1 # 0.99999999999


# 0.4444444444 + 0.66666666666
# 0.999999999999
# 1.0

def minus(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def make_error():
    raise IndexError()

def create_table(query):
    # check if table exists
    raise sqlite3.IntegrityError

def say_hello():
    name = input("enter name? ")
    return f"hello {name}"