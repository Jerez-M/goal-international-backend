import re


def validate_id(string):
    regex = re.compile(r"^\d{2}-\d{5,8}[A-Z]\d{2,10}$")
    return regex.match(string) is not None
