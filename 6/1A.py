#!/usr/bin/env python3

from sense_hat import SenseHat
import time

sense = SenseHat()
delay_val = 1.0

w = (255, 255, 255)
n = (0, 0, 0)
# fmt: off
on = [
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w,
    w, w, w, w, w, w, w, w
]

off = [
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


def delay(event):
    global delay_val
    if event.action == "pressed":
        delay_val = 0.2
    elif event.action == "released":
        delay_val = 1.0


def d_delay(event):
    global delay_val
    if event.action == "pressed":
        delay_val = 0.5
    elif event.action == "released":
        delay_val = 2.0


def u_delay(event):
    global delay_val
    if event.action == "pressed":
        delay_val = 0.1
    elif event.action == "released":
        delay_val = 0.5


def l_delay(event):
    global delay_val
    if event.action == "pressed":
        delay_val = 1.0
    elif event.action == "released":
        delay_val = 0.3


def r_delay(event):
    global delay_val
    if event.action == "pressed":
        delay_val = 0.3
    elif event.action == "released":
        delay_val = 1.0


def main():
    sense.stick.direction_middle = delay
    sense.stick.direction_down = d_delay
    sense.stick.direction_up = u_delay
    sense.stick.direction_left = l_delay
    sense.stick.direction_right = r_delay
    while True:
        sense.set_pixels(on)
        time.sleep(delay_val)
        sense.set_pixels(off)
        time.sleep(delay_val)


if __name__ == "__main__":
    main()
