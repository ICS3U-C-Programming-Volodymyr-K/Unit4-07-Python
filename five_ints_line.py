#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 05, 2, 2025
# This program  displays numbers from 1000 to 2000.


def main():
    # Initiliazes value needed for making newline character
    count = 0
    # For loop which is responsible for display of numbers
    for counter in range(1000, 2001):
        # Prints off the numbers given in a for loop and makes a white space between them
        print(counter, end=" ")
        # Controls the amount of numbers per line
        count = count + 1
        # Creates a newline character whenever there is 5 numbers in a line.
        if count % 5 == 0:
            print()


if __name__ == "__main__":
    main()
