#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: May 2021
# This program prints all the RGB values and uses nested loops


def main():
    # This function prints the values
    loop_counter1 = 0
    loop_counter2 = 0
    loop_counter3 = 0

    # Process & Output
    print("This program prints all the RGB values.")
    print("")
    for loop_counter1 in range(255 + 1):
        for loop_counter2 in range(255 + 1):
            for loop_counter3 in range(255 + 1):
                print("RGB({0},{1},{2})".format(
                    loop_counter1, loop_counter2, loop_counter3))
    print("")
    print("\nDone.")


if __name__ == "__main__":
    main()
