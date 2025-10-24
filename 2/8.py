#!/usr/bin/env python3


def fibonacci(n):
    a = 0
    b = 1

    if n == 0:
        return a
    elif n == 1:
        return b
    else:
        for _ in range(1, n):
            c = a + b
            a = b
            b = c
        return c


def main():
    for i in range(0, 10):
        print(fibonacci(i))


if __name__ == "__main__":
    main()
