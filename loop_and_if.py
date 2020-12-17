#!/usr/bin/env python3

# Created by Ryan Nguyen
# Created on Decemebr 2020
# This program prints every integer from
#   1000 to 2000 with 5 integers per line


def main():
    # this function uses a For and if statement together

    for counter in range(1000, 2000 + 1):
        if (counter + 1) % 5 != 0:
            print("{} ".format(counter), end="")
        else:
            print("{} ".format(counter))


if __name__ == "__main__":
    main()
