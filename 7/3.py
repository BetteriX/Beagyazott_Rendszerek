#!/usr/bin/env python3

from sense_hat import SenseHat
import random
from time import sleep

sense = SenseHat()
speed = 0.4
line = [7, 4]
up_down = -1

w = (0, 0, 0)
r = (255, 0, 0)
b = (0, 0, 255)
# fmt: off
game_space = [
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,b,b,w,w,w
]
# fmt: on


def update_space(x, y, colour):
    # index element from coordinate
    p = 8 * x + y
    game_space[p] = colour
    sense.set_pixels(game_space)


def left(event):
    if event.action == "pressed":
        # the line reached the left side
        if line[0] - 1 == 0:
            pass
        # move line one position left
        else:
            update_space(line[0], line[1], w)
            line[1] -= 1
            update_space(line[0], line[1] - 1, b)


def right(event):
    if event.action == "pressed":
        # the line reached the right side
        if line[1] + 1 == 8:
            pass
        # move line one position left
        else:
            update_space(line[0], line[1] - 1, w)
            line[1] += 1
            update_space(line[0], line[1], b)


def main():
    score = 0
    sense.stick.direction_left = left
    sense.stick.direction_right = right
    sense.clear()
    sense.set_pixels(game_space)
    game_alive = True

    while game_alive:
        # initialize position and direction of the ball
        # (x,y) – ball coordinate, d - direction
        x = 0
        y = random.randint(0, 7)
        # random.choice() – randomly selects a value from a list
        d = random.choice([-1, 1])

        # put the ball into the game space
        update_space(x, y, r)
        # while the ball is in the game space
        while True:
            sleep(speed)
            update_space(x, y, w)

            # redraw paddle
            update_space(line[0], line[1], b)
            update_space(line[0], line[1] - 1, b)

            # Contacted the linef
            if x == 0:
                up_down = 1
            if x == 7:
                if y == line[1] - 1 or y == line[1]:
                    up_down = -1
                    score += 1
                else:
                    # ball is out of the space
                    game_alive = False
                    break

            # ball reached the right side of the space
            if y == 7 and d == 1:
                d = -1
            # ball reached the left side of the space
            elif y == 0 and d == -1:
                d = 1

            y += d
            x += up_down
            update_space(x, y, r)

    sense.clear()
    sense.show_message("Game over!", scroll_speed=0.05, back_colour=w)
    sense.show_message("Score: " + str(score), scroll_speed=0.01, back_colour=w)


if __name__ == "__main__":
    main()
