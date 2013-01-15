import random


class CannotGeneratePassword(Exception):
    pass


class RequestedPasswordTooLong(CannotGeneratePassword):
    pass


def generate_password(characters, min_length, max_length, repeats_allowed=True):

    # make sure we are dealing with a set here, it is important that the character set has no duplicates
    characters = set(characters)
    # except now, we need it as a list so we can index it!
    characters = list(characters)

    if not repeats_allowed:
        if min_length > len(characters):
            raise RequestedPasswordTooLong

        max_length = min(max_length, len(characters))

    length = random.randint(min_length, max_length)

    if repeats_allowed:
        password = []
        while len(password) < length:
            password.append( random.choice(characters) )
    else:
        password = random.sample(characters, length)

    return ''.join(password)