#!/usr/bin/env python3

from sense_hat import SenseHat


def main():
    sense = SenseHat()
    p = round(sense.get_pressure(), 1)
    p0 = 1013.25

    h = 44331 * (1 - (p / p0) ** (1 / 5.2558))
    print(h)


if __name__ == "__main__":
    main()
