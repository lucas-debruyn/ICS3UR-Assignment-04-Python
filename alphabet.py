#!/usr/bin/env python3

# Created by: Lucas DeBruyn
# Created on: November 2022
# This program tells a user if a letter a consonant or vowel.


def main():
    # This function determines if a letter a consonant or vowel

    # Input
    user_letter = input("Enter a letter (single digit/uppercase): ")

    # Process and Output
    if (
        user_letter == "A"
        or user_letter == "E"
        or user_letter == "I"
        or user_letter == "O"
        or user_letter == "U"
    ):
        print("\nYour letter is a vowel!")
    elif (
        user_letter == "B"
        or user_letter == "C"
        or user_letter == "D"
        or user_letter == "F"
        or user_letter == "G"
        or user_letter == "H"
        or user_letter == "I"
        or user_letter == "J"
        or user_letter == "K"
        or user_letter == "L"
        or user_letter == "M"
        or user_letter == "N"
        or user_letter == "P"
        or user_letter == "Q"
        or user_letter == "R"
        or user_letter == "S"
        or user_letter == "T"
        or user_letter == "V"
        or user_letter == "W"
        or user_letter == "X"
        or user_letter == "Z"
    ):
        print("\nYour letter is a consonant!")
    elif user_letter == "Y":
        print("\nYour letter is sometimes a vowel and sometimes a consonant!")
    else:
        print("\nPlease input a valid letter.")

    print("\nDone.")


if __name__ == "__main__":
    main()
