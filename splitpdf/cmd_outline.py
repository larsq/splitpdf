"""Parse arguments."""
import argparse
import os

from outline_pdf import outline


def existing_file(str):
    """Check if str is an existing file."""
    if not os.path.isfile(str):
        raise argparse.ArgumentTypeError('%r must be an existing file' % str)

    return str


parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--in', type=existing_file, dest='infile')


def main():
    """Main command."""
    args = parser.parse_args()

    outline(args.infile)


if __name__ == '__main__':
    main()
