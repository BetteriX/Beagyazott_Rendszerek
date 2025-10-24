#!/usr/bin/env python3


def decipher_caesar(text):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    values = {}

    for key in range(1, 26):
        decrypted = ""

        for c in text:
            position = alphabet.find(c)
            new_position = (position - key) % len(alphabet)
            decrypted += alphabet[new_position]

        values[key] = decrypted
        # print(f"Key {key}: {decrypted}")

    return values


def main():
    result = decipher_caesar("iqfihhih")

    for key, message in result.items():
        print(f"Key {key}: {message}")


if __name__ == "__main__":
    main()
