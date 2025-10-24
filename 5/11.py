#!/usr/bin/env python3

from sense_hat import SenseHat
import time
import math

sense = SenseHat()
w = (0, 0, 0)
p = (255, 192, 203)
dg = (6, 64, 43)
g = (212, 222, 149)

# fmt: off
Cat_1 = [
        w, w, w, w, w, w, w, w,
        p, w, w, w, w, w, w, w,
        w, p, w, w, p, w, p, w,
        w, p, dg, dg, p, g, g, w,
        w, dg, dg, dg, g, w, g, dg,
        w, dg, dg, dg, dg, g, g, w,
        w, dg, w, dg, w, dg, w, w,
        w, w, w, w, w, w, w, w
]
# fmt: on

# fmt: off
Cat_2 = [
        w, w, w, w, w, w, w, w,
        p, w, w, w, w, w, w, w,
        w, p, w, w, p, w, p, w,
        w, p, dg, dg, p, g, g, w,
        w, dg, dg, dg, g, w, g, dg,
        w, dg, dg, dg, dg, g, g, w,
        w, w, dg, w, dg, w, w, w,
        w, w, w, w, w, w, w, w
]
# fmt: on


def Cat():
    sense.set_pixels(Cat_1)
    time.sleep(0.5)
    sense.set_pixels(Cat_2)
    time.sleep(0.5)


def main():
    while True:
        acceleration = sense.get_accelerometer_raw()

        x = acceleration["x"]
        y = acceleration["y"]
        z = acceleration["z"]

        x = round(x, 0)
        y = round(y, 0)
        z = round(z, 0)

        F = math.sqrt(x**2 + y**2 + z**2)

        if F > 1.2:
            Cat()


if __name__ == "__main__":
    main()
