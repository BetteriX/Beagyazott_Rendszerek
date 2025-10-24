#!/usr/bin/env python3

from sense_hat import SenseHat
import random
from time import sleep


sense = SenseHat()

o = (0, 0, 0)  # no color
b = (0, 0, 255)

# fmt:  off
one_img = [
            o,o,o,o,o,o,o,o,
            o,o,o,o,o,o,o,o,
            o,o,o,o,o,o,o,o,
            o,o,o,b,b,o,o,o,
            o,o,o,b,b,o,o,o,
            o,o,o,o,o,o,o,o,
            o,o,o,o,o,o,o,o,
            o,o,o,o,o,o,o,o
]
two_img = [
            b,b,o,o,o,o,o,o,
            b,b,o,o,o,o,o,o,
            o,o,o,o,o,o,o,o,
            o,o,o,o,o,o,o,o,
            o,o,o,o,o,o,o,o,
            o,o,o,o,o,o,o,o,
            o,o,o,o,o,o,b,b,
            o,o,o,o,o,o,b,b
]
three_img = [
            b,b,o,o,o,o,o,o,
            b,b,o,o,o,o,o,o,
            o,o,o,o,o,o,o,o,
            o,o,o,b,b,o,o,o,
            o,o,o,b,b,o,o,o,
            o,o,o,o,o,o,o,o,
            o,o,o,o,o,o,b,b,
            o,o,o,o,o,o,b,b
]
four_img = [
            b,b,o,o,o,o,b,b,
            b,b,o,o,o,o,b,b,
            o,o,o,o,o,o,o,o,
            o,o,o,o,o,o,o,o,
            o,o,o,o,o,o,o,o,
            o,o,o,o,o,o,o,o,
            b,b,o,o,o,o,b,b,
            b,b,o,o,o,o,b,b
]
five_img = [
            b,b,o,o,o,o,b,b,
            b,b,o,o,o,o,b,b,
            o,o,o,o,o,o,o,o,
            o,o,o,b,b,o,o,o,
            o,o,o,b,b,o,o,o,
            o,o,o,o,o,o,o,o,
            b,b,o,o,o,o,b,b,
            b,b,o,o,o,o,b,b
] 
six_img = [
            b,b,o,o,o,o,b,b,
            b,b,o,o,o,o,b,b,
            o,o,o,o,o,o,o,o,
            b,b,o,o,o,o,b,b,
            b,b,o,o,o,o,b,b,
            o,o,o,o,o,o,o,o,
            b,b,o,o,o,o,b,b,
            b,b,o,o,o,o,b,b
  ]
# fmt: on

images = {1: one_img, 2: two_img, 3: three_img, 4: four_img, 5: five_img, 6: six_img}


def roll_animation():
    randoms = random.sample(range(1, 6), 4)

    for val in randoms:
        sense.set_pixels(images[val])
        sleep(0.75)


def number_gen(event):
    if event.action == "pressed":
        val = random.randint(1, 6)
        print(val)
        roll_animation()
        sense.set_pixels(images[val])

        sleep(2)
        sense.clear()


def main():
    while True:
        for event in sense.stick.get_events():
            if event.direction == "middle":
                number_gen(event)


if __name__ == "__main__":
    main()
