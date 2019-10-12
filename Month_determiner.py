#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Oct 2019
# This program determines which month a number is based on user input


def main():
    # this function determines which month a number is based on user input

    # input
    month = int(input("Enter the number of a month (ex: April= 4): "))

    # process and output
    print("your month is")
    if month == 1:
        print("January")
    elif month == 2:
        print("February")
    elif month == 3:
        print("March")
    elif month == 4:
        print("April")
    elif month == 5:
        print("May")
    elif month == 6:
        print("June")
    elif month == 7:
        print("July")
    elif month == 8:
        print("August")
    elif month == 9:
        print("September")
    elif month == 10:
        print("October")
    elif month == 11:
        print("November")
    elif month == 12:
        print("December")
    else:
        print("Error, your number can not be assigned to a month")


if __name__ == "__main__":
    main()
