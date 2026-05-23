def xor_bytes(data: bytes, key: bytes) -> bytes:
    if len(data) != len(key):
        raise ValueError("Data and key must be the same length")
    return bytes(d ^ k for d, k in zip(data, key))
