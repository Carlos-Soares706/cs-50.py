def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    answer = answer.strip().lower()  # Remove leading/trailing whitespace and convert to lowercase

    if answer == "42" or answer == "forty-two" or answer == "forty two":
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
