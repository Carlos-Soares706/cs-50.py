# playback.py

def main():
    # Prompt the user for input
    user_input = input("Please enter some text: ")

    # Replace each space with three periods
    modified_input = user_input.replace(" ", "...")

    # Output the modified input
    print(modified_input)

if __name__ == "__main__":
    main()
