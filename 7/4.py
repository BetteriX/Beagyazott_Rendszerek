#!/usr/bin/env python3

from sense_hat import SenseHat
import random
from time import sleep

sense = SenseHat()
speed = 0.4
snake = [[4, 5]]
apple = [random.randint(0, 7), random.randint(0, 7)]
direction = [0, -1]

w = (0, 0, 0)
g = (0, 255, 0)
r = (255, 0, 0)

# fmt: off
game_space = [
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w,
    w,w,w,w,w,w,w,w
]
# fmt: on


def update_space(x, y, color):
    game_space[8 * x + y] = color
    sense.set_pixels(game_space)


def left(event):
    if event.action == "pressed" and direction != [0, 1]:
        direction[0], direction[1] = 0, -1


def right(event):
    if event.action == "pressed" and direction != [0, -1]:
        direction[0], direction[1] = 0, 1


def up(event):
    if event.action == "pressed" and direction != [1, 0]:
        direction[0], direction[1] = -1, 0


def down(event):
    if event.action == "pressed" and direction != [-1, 0]:
        direction[0], direction[1] = 1, 0


sense.stick.direction_left = left
sense.stick.direction_right = right
sense.stick.direction_up = up
sense.stick.direction_down = down


def main():
    global apple
    score = 0
    game_alive = True
    while game_alive:
        sleep(speed)

        tail_x, tail_y = snake[-1]
        update_space(tail_x, tail_y, w)

        update_space(apple[0], apple[1], r)

        new_x = snake[0][0] + direction[0]
        new_y = snake[0][1] + direction[1]

        if new_x < 0 or new_x > 7 or new_y < 0 or new_y > 7 or [new_x, new_y] in snake:
            game_alive = False
            break

        snake.insert(0, [new_x, new_y])

        if [new_x, new_y] == apple:
            score += 1

            free_spaces = [
                [i, j] for i in range(8) for j in range(8) if [i, j] not in snake
            ]
            if free_spaces:
                apple = random.choice(free_spaces)
                update_space(apple[0], apple[1], r)
        else:
            snake.pop()

        for tail in snake:
            update_space(tail[0], tail[1], g)

    sense.clear()

    if score == 64:
        sense.show_message("Congratulation You Won!", scroll_speed=0.05, back_colour=w)
    else:
        sense.show_message("Game over!", scroll_speed=0.05, back_colour=w)
        sense.show_message("Score: " + str(score), scroll_speed=0.01, back_colour=w)


if __name__ == "__main__":
    main()
