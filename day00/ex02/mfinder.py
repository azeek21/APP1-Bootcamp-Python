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

    try:
        lines = []
        for i in range(100):
            inp = input()
            if len(inp) != 5 and i < 3:
                print("Bad dimensions for the picture. Picture should be 5 chars long per line.")
                return
            elif len(inp) == 5 and i < 3:
                lines.append(inp)
            elif len(inp) == 0 and i >= 3:
                break
            elif len(inp) > 0 and i >= 3:
                print("Bad dmensions for the picture. Height of the picture should be 3 lines high.")
    except Exception as e:
        print("FATAL: something went wrong, exiting ...")
        return
    print(is_2dmap(lines) and is_m('\n'.join(lines)))


if __name__ == "__main__":
    main()
