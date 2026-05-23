import os
from core.cipher import xor_bytes
from core.key import generate_key
from core.file_utils import read_bytes, write_bytes

def main():
    plaintext_path = input("Enter plaintext file name: ").strip()

    if not os.path.splitext(plaintext_path)[1]:
        plaintext_path += ".txt"

    while not os.path.exists(plaintext_path):
        print(f"{plaintext_path} doesn't exist.")
        plaintext_path = input("\nEnter valid file name: ").strip()

        
    key_path = "keys/key.bin"
    cipher_path = "encrypted/cipher.bin"
    decrypted_path = "decrypted/decrypted.txt"
    
    data = read_bytes(plaintext_path)
    
    key = generate_key(len(data))
    write_bytes(key_path, key)
    
    # Encrypt
    cipher = xor_bytes(data, key)
    write_bytes(cipher_path, cipher)
    
    # Decrypt
    decrypted = xor_bytes(cipher, key)
    write_bytes(decrypted_path, decrypted)
    
    # Status messages
    print("Encryption complete.")
    
    print(f"\nKey saved to: {key_path}")
    print(f"Ciphertext saved to: {cipher_path}")
    print(f"Decrypted output saved to: {decrypted_path}")

if __name__ == "__main__":
    main()
