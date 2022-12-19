def main():
    import sys

    # argument check
    if len(sys.argv) != 2:
        print("Only 1 argument (number of lines) required !")
        return

    # check if number of lines is an actual number
    if not sys.argv[1].isdigit():
        print(f"Expected a number that indicates number of lines to read.\n{sys.argv[1]} is not a number !")
        return

    # extracting number of lines from argv
    lines_count = int(sys.argv[1])

    # getting user input lines_count times from standart input
    for _ in range(lines_count):
        line = input()
        # checking if input is exactly 32 chars and starts with ONLY 5 zeros
        if len(line) == 32 and line.startswith('00000') and line[5] != '0':
            print(line)


if __name__ == "__main__":
    main()


# NOTE: above solution is almost realtime as we don't store more than one input per loop