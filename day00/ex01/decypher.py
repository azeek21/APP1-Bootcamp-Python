# The secret location was a concated string of ever first character of the message
# to decypher the message, we need to print first letter of every word of the message without spaces between

def main():
    import sys

    # checking number of arguments
    if len(sys.argv) != 2:
        return print("Expected one argument. Found ", len(sys.argv))

    # removing \n and \t from string as messages may include them
    sys.argv[1] = sys.argv[1].strip().replace('\n', ' ').replace('\t', ' ')

    # one liner code below
    # print(''.join([i[0] for i in sys.argv[1].split(' ') if not i[0].isdigit()])) 

    # more understandable version
    # extract string from args and create array of words by splitting the string by ' ' (space)
    string = sys.argv[1].split(' ')

    for word in string:
        # check if word starts with alphabetic char so we can print it
        if word[0].isalpha():
            print(word[0], end='') # end='' disables default adding \n for print function. Print adds \n char after every execution by default


if __name__ == '__main__':
    main()
