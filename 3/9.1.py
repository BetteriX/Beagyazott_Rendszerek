#!/usr/bin/env python3


def factorize(n):
    factors = []
    for i in range(2, int(n / 2) + 1):
        if n % i == 0:
            factors.append(i)

    return factors


def main():
    print(factorize(63))


if __name__ == "__main__":
    main()
