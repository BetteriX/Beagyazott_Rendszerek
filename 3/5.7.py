#!/usr/bin/env python3
from random import randint

ALPHABET = "abcdefghijklmnopqrstuvwxyz"


def generate_otp(characters):
    with open("otp.txt", "w") as f:
        for i in range(characters):
            f.write(str(randint(0, 26)) + "\n")


def load_otp():
    with open("otp.txt", "r") as f:
        contents = f.read().splitlines()
    return contents


def encrypt(message, key):
    ciphertext = ""
    for position, character in enumerate(message):
        if character not in ALPHABET:
            ciphertext += character
        else:
            encrypted = (ALPHABET.index(character) + int(key[position])) % len(ALPHABET)
            ciphertext += ALPHABET[encrypted]
    return ciphertext


def main():
    while True:
        message = input("Please enter a message: ")
        if message == "q":
            break
        else:
            generate_otp(len(message))
            key = load_otp()
            encry_message = encrypt(message, key)
            negativ_key = [-int(k) for k in key]  # Egyenként negatívá alakítja
            decry_message = encrypt(encry_message, negativ_key)

        print("Encrypted message: ", encry_message)
        print("Decrypted message: ", decry_message)


if __name__ == "__main__":
    main()
