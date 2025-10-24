#!/usr/bin/env python3

from sense_hat import SenseHat
from random import randint
from time import sleep


def random_colour():
    # randint - random integer between an interval
    random_red = randint(0, 255)
    random_green = randint(0, 255)
    random_blue = randint(0, 255)
    return (random_red, random_green, random_blue)


def main():
    sense = SenseHat()

    sense.show_letter("Z", random_colour())
    sleep(1)

    sense.show_letter("S", random_colour())
    sleep(1)

    sense.show_letter("O", random_colour())
    sleep(1)

    sense.show_letter("L", random_colour())
    sleep(1)

    sense.show_letter("T", random_colour())
    sleep(1)

    sense.clear()


if __name__ == "__main__":
    main()
