import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    check_command()

    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit('Input does not exist')

    shirt = Image.open('shirt.png')
    resize = shirt.size

    muppet = ImageOps.fit(imagefile, resize)
    muppet.paste(shirt, shirt)

    muppet.save(sys.argv[2])

def check_command():
    len_argv = len(sys.argv)

    if len_argv < 3:
        sys.exit("Too few command-line arguments")
    if len_argv > 3:
        sys.exit("Too many command-line arguments")

    file_bef = splitext(sys.argv[1])
    file_aft = splitext(sys.argv[2])

    if not extension(file_bef[1]):
        sys.exit('Invalid input')
    if not extension(file_aft[1]):
        sys.exit('Invalid output')

    if file_bef[1].lower() != file_aft[1].lower():
        sys.exit('Input and output have different extensions')

def extension(file_ext):
    extensions = ['.jpg', '.jpeg', '.png']
    return file_ext.lower() in extensions

if __name__ == "__main__":
    main()
