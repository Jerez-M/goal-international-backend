import random
import string

def generate_organisation_number(organisation_identifier, db_number, sequence_number_length, alphanumeric_length):
    # Generate sequential number
    sequential_number = str(random.randint(1, 10 ** sequence_number_length)).zfill(sequence_number_length)

    a = random.randint(0, 9)
    b = random.randint(0, 9)
    c = random.randint(0, 9)
    d = random.randint(0, 9)

    random_number = f'{a}{b}{c}{d}{d}'

    # Generate random alphanumeric code
    alphanumeric_code = ''.join(
        random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=alphanumeric_length))

    alphanumeric_code_2 = ''.join(
        random.choices(string.ascii_uppercase + string.digits, k=alphanumeric_length))

    # Combine organisation identifier, sequential number, and alphanumeric code
    organisation_number = f"{organisation_identifier}{db_number}-{sequential_number}-{alphanumeric_code}-{random_number}-{alphanumeric_code_2}"

    return organisation_number
