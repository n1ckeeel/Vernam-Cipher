import os


def read_bytes(path: str) -> bytes:
    with open(path, "rb") as f:
        return f.read()

def write_bytes(path: str, data: bytes):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
