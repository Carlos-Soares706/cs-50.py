import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Regular expression to check if the input is a valid IPv4 address
    if re.match(r"^(\d{1,3}\.){3}\d{1,3}$", ip):
        number_list = ip.split('.')
        for num in number_list:
            if int(num) < 0 or int(num) > 255:
                return False
        return True
    return False

if __name__ == "__main__":
    main()
