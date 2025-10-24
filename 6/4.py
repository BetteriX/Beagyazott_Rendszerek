#!/usr/bin/env python3

from sense_hat import SenseHat
import time
import random

sense = SenseHat()

n = (0, 0, 0)
b = (0, 0, 255)

# fmt: off
space = [
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n
]
# fmt: on


def shift_down():
    global space

    for row in range(7, 0, -1):
        for col in range(8):
            space[row * 8 + col] = space[(row - 1) * 8 + col]

    for col in range(8):
        space[col] = n

    sense.set_pixels(space)


def main():
    while True:
        pos = random.randint(0, 7)
        space[pos] = b

        sense.set_pixels(space)
        time.sleep(0.5)
        shift_down()


if __name__ == "__main__":
    main()
