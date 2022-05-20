#!/usr/bin/env python3

# Created by: Aleksandr Ten
# Created on: May 2022
# This program generates random arrays and averages them out


import random


def main():
    # this function finds the average of 10 random numbers

    number_array = []

    print("This program generates 10 random numbers and finds its average.\n")

    # process
    for counter in range(0, 10):
        random_number = random.randint(0, 100)
        number_array.append(random_number)
        print("Random number generated: {}".format(random_number))

    average = sum(number_array) / 10

    # output
    print("\nThe average is {0:.2f}.".format(average))

    print("\nDone")


if __name__ == "__main__":
    main()
