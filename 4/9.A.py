#!/usr/bin/env python3

from sense_hat import SenseHat
from time import sleep


def main():
    sense = SenseHat()

    w = (255, 255, 255)  # white
    r = (255, 0, 0)  # blue

    while True:
        # go throw all joystick’s events
        for event in sense.stick.get_events():
            # Check if the joystick was pressed
            if event.action == "pressed":
                # Check which direction
                if event.direction == "up":  # Up arrow
                    # fmt: off
                    Up = [
                        w, w, w, w, w, w, w, w,
                        w, w, w, r, w, w, w, w,
                        w, w, r, r, r, w, w, w,
                        w, r, w, r, w, r, w, w,
                        w, w, w, r, w, w, w, w,
                        w, w, w, r, w, w, w, w,
                        w, w, w, r, w, w, w, w,
                        w, w, w, w, w, w, w, w
                    ]
                    # fmt: on

                    sense.set_pixels(Up)
                elif event.direction == "down":  # Down arrow
                    # fmt: off
                    Down = [
                        w, w, w, w, w, w, w, w,
                        w, w, w, r, w, w, w, w,
                        w, w, w, r, w, w, w, w,
                        w, w, w, r, w, w, w, w,
                        w, r, w, r, w, r, w, w,
                        w, w, r, r, r, w, w, w,
                        w, w, w, r, w, w, w, w,
                        w, w, w, w, w, w, w, w
                    ]
                    # fmt: on

                    sense.set_pixels(Down)
                elif event.direction == "left":  # Left arrow
                    # fmt: off
                    Left = [
                        w, w, w, w, w, w, w, w,
                        w, w, w, w, w, w, w, w,
                        w, w, w, w, r, w, w, w,
                        w, w, w, r, w, w, w, w,
                        w, w, r, r, r, r, r, w,
                        w, w, w, r, w, w, w, w,
                        w, w, w, w, r, w, w, w,
                        w, w, w, w, w, w, w, w
                    ]
                    # fmt: on

                    sense.set_pixels(Left)
                elif event.direction == "right":  # Right arrow
                    # fmt: off
                    Right = [
                        w, w, w, w, w, w, w, w,
                        w, w, w, w, w, w, w, w,
                        w, w, w, r, w, w, w, w,
                        w, w, w, w, r, w, w, w,
                        w, r, r, r, r, r, w, w,
                        w, w, w, w, r, w, w, w,
                        w, w, w, r, w, w, w, w,
                        w, w, w, w, w, w, w, w
                    ]
                    # fmt: on

                    sense.set_pixels(Right)
                # Wait a while and then clear the screen
                sleep(0.5)
                sense.clear()


if __name__ == "__main__":
    main()
