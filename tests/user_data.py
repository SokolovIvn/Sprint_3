import pytest
import random


def generate_name():
    name = f"Name{random.randint(100, 999)}"
    return name


def generate_password():
    pswd = str(random.randint(100000, 999999))
    return pswd


def get_fixture_email():
    return "testtest@yy.ru"


def get_fixture_pswd():
    return "123456"

