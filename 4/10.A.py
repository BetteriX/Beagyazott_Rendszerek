#!/usr/bin/env python3

from sense_hat import SenseHat
from time import sleep

sense = SenseHat()


# Define the functions
# def red():
#    # set a given color on all LEDs
#    sense.clear(255, 0, 0)


def blinking_red_heart():
    w = (255, 255, 255)  # white
    r = (255, 0, 0)  # red

    while True:
        # fmt: off
        Heart = [
            w, w, w, w, w, w, w, w,
            w, r, r, w, w, r, r, w,
            r, r, r, r, r, r, r, r,
            r, r, r, r, r, r, r, r,
            w, r, r, r, r, r, r, w,
            w, w, r, r, r, r, w, w,
            w, w, w, r, r, w, w, w,
            w, w, w, w, w, w, w, w
        ]
        # fmt: on

        # change all 64 LEDs
        sense.set_pixels(Heart)
        sleep(0.5)
        sense.clear(255, 255, 255)
        sleep(0.5)


def blue():
    sense.clear(0, 0, 255)


def green():
    sense.clear(0, 255, 0)


def yellow():
    sense.clear(255, 255, 0)


def main():
    sense.stick.direction_up = blinking_red_heart
    sense.stick.direction_down = blue
    sense.stick.direction_left = green
    sense.stick.direction_right = yellow
    sense.stick.direction_middle = sense.clear

    while True:
        pass


if __name__ == "__main__":
    main()
