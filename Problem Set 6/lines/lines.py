import sys

def main():
    check_command()

    try:
        with open(sys.argv[1], 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    counter = 0
    for line in lines:
        if not check_false_lines(line):
            counter += 1
    print(counter)

def check_command():
    len_argv = len(sys.argv)

    if len_argv < 2:
        sys.exit("Too few command-line arguments")

    if len_argv > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith('.py'):
        sys.exit("Not a Python file")

def check_false_lines(line):
    if line.isspace():
        return True
    if line.lstrip().startswith('#'):
        return True
    return False

if __name__ == "__main__":
    main()
