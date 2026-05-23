import os


def generate_key(length: int) -> bytes:
    return os.urandom(length)
