#!/usr/bin/env python3

from sense_hat import SenseHat


def main():
    sense = SenseHat()

    w = (255, 255, 255)  # white
    r = (255, 0, 0)  # red

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


if __name__ == "__main__":
    main()
