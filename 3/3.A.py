#!/usr/bin/env python3


# def caesar(msg, key):
#    alphabet = "abcdefghijklmnopqrstuvwxyz"
#    new_message = ""
#    for c in msg:
#        position = alphabet.find(c)
#        new_position = (position + key) % len(alphabet)
#        new_character = alphabet[new_position]
#        new_message += new_character
#    return new_message


def caesar(msg, key):
    new_message = ""
    for c in msg:
        ascii_code = ord(c)  # Az aktuális karakter ascii kódja
        new_message += chr(
            ascii_code + key
        )  # Eltolja a key-el majd átalakítja karakteré
    return new_message


def main():
    key = 3
    while True:
        message = input("Please enter a message: ")
        if message == "q":
            break
        else:
            encry_message = caesar(message, key)
        print("Encrypted message: ", encry_message)


if __name__ == "__main__":
    main()
