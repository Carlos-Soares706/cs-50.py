import re
#import sys


def main():
    print(count(input("Text: ")))


def count(s):
    um_pattern = re.findall(r'\bum\b', s.lower())

    return len(um_pattern)


if __name__ == "__main__":
    main()

