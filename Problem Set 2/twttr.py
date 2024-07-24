def main():

    text = input("Input: ")

    # Call the function
    mssg = shorten(text)

    print ("Output: ", mssg)


def shorten (text):

    vogais = ['a', 'e', 'i', 'o', 'u']

    new_str = ''

    for i in text:
        if i.lower() in vogais:
            continue
        else:
            new_str += i

    return new_str

if __name__ == "__main__":
    main()
