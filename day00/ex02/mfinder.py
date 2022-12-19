from argparse import ArgumentParser
import sys


TEMPLATE = "*000*\n**0**\n*0*0*"


# check if string includes M
def is_m(line: str) -> bool:
    global TEMPLATE

    # looping over Template which has M in it and comparing the input
    # if input does'n match the tepmlate, we return False else True
    for i, char in enumerate(TEMPLATE):
        if char == '*' and line[i] != char or char != '*' and line[i] == '*':
            return False

    return True


# checking the map for height and withd sizes
def is_2dmap(line) -> bool:
    x = len(line)
    if x != 3:
        return False

    for i in range(x):
        if len(line[i].replace('\n', '')) != 5:
            return False

    return True


def main():
    # initialize parser instance
    parser = ArgumentParser()

    # adding argument "filename" to read from arguments
    parser.add_argument('filename', help="name  or path to a file to read the M from")

    filename = parser.parse_args().filename

    # reading from file with a little bit of safety
    try:
        with open(filename, "r") as file:
            line = file.readlines()
    except IsADirectoryError as e:
        print(e)
        return
    except FileNotFoundError as e:
        print(e)
        return

    # checks the map and existance of M in it.
    # as script is executed from left to right below
    # is_m() function will not be called if is_2dmap() returns false
    # so below line is safe and will not execute on wrong map.
    print(is_2dmap(line) and is_m(''.join(line)))


if __name__ == "__main__":
    main()
