#!/usr/bin/env python3

from sense_hat import SenseHat
import time

sense = SenseHat()
p = [2, 3]
light_len = 3
space_size = 8
speed = 1 / 7

r = (255, 0, 0)
n = (0, 0, 0)

# fmt: off
space = [
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    r, r, r, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n
]
# fmt: on


def shift_right():
    global p, space

    for i in range(light_len):
        x = p[0] - i
        space[p[1] * space_size + x] = n

    p[0] += 1

    for i in range(light_len):
        x = p[0] - i
        space[p[1] * space_size + x] = r

    sense.set_pixels(space)


def shift_left():
    global p, space

    for i in range(light_len):
        x = p[0] - i
        space[p[1] * space_size + x] = n

    p[0] -= 1

    for i in range(light_len):
        x = p[0] - i
        space[p[1] * space_size + x] = r

    sense.set_pixels(space)


def main():
    global p
    while True:
        while True:
            shift_right()
            time.sleep(speed)
            if p[0] == space_size - 1:
                break

        while True:
            shift_left()
            time.sleep(speed)
            if p[0] == light_len - 1:
                break


if __name__ == "__main__":
    main()
