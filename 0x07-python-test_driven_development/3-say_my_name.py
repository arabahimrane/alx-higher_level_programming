#!/usr/bin/python3
""" function that prints My name is <first name> <last name> """


def say_my_name(first_name, last_name=""):
    """You can say my Name please"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
