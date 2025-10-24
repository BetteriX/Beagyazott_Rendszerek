#!/usr/bin/env python3

from sense_hat import SenseHat
from time import sleep


def calculate_P(p, t, h):
    return p * (1 - ((0.0065 * h) / (t + 0.0065 * h + 273.15))) ** (-5.257)


def main():
    sense = SenseHat()
    while True:
        t1 = round(sense.get_temperature(), 1)
        p1 = round(sense.get_pressure(), 1)
        # h = sense.get_humidity()
        h = 125

        # h = round(h, 1)

        P0 = calculate_P(p1, t1, h)

        sleep(3 * 60 * 60)  # 3 hours

        t2 = round(sense.get_temperature(), 1)
        p2 = round(sense.get_pressure(), 1)
        # h = sense.get_humidity()
        h = 125

        P1 = calculate_P(p2, t2, h)

        kulonbseg = P1 - P0

        Z = 0
        if kulonbseg < -1.6 and 985 <= P0 <= 1050:
            Z = 127 - 0.12 * P0
        elif kulonbseg > 1.6 and 947 <= P0 <= 1030:
            Z = 185 - 0.16 * P0
        elif 960 <= P0 <= 1033:
            Z = 144 - 0.13 * P0


if __name__ == "__main__":
    main()
