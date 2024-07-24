import sys
import csv

def main():

    check_command()

    output = []

    try:

        with open(sys.argv[1], 'r') as before:
            reader = csv.DictReader(before)
            for row in reader:

                split_name = row['name']. split(',')
                output.append({'first': split_name[1].lstrip(), 'last': split_name[0], 'house': row['house']})


    except FileNotFoundError:
        sys.exit('File does not exit')

    with open(sys.argv[2], 'w') as after:
        writer = csv.DictWriter(after, fieldnames=['first', 'last', 'house'])

        writer.writerow({'first':'first', 'last':'last', 'house':'house'})

        for row in output:
            writer.writerow({'first' :row['first'], 'last': row['last'], 'house': row['house']})


def check_command():

    len_argv = len(sys.argv)

    if len_argv < 3:
        sys.exit("Too few command-line arguments")
    if len_argv > 3:
        sys.exit("Too many command-line arguments")

    for i in range(1, 2):
        if '.csv' not in sys.argv[i]:
            sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()
