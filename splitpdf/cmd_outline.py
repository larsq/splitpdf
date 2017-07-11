"""Parse arguments."""
import argparse
import os

from outline_pdf import outline


def existing_file(str):
    """Check if str is an existing file."""
    if not os.path.isfile(str):
        raise argparse.ArgumentTypeError('%r must be an existing file' % str)

    return str


def positve_number(str):
    """Check if str is a positive number."""
    try:
        parsed = int(str)
        if(parsed < 1):
            raise argparse.ArgumentTypeError(
                '%r must be a positive number' % str)
        return parsed
    except ValueError:
        raise argparse.ArgumentTypeError('%r must be a number' % str)


parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--in', type=existing_file, dest='infile')
parser.add_argument('--levels', type=positve_number, dest='levels', default=1)
parser.add_argument('--split', action='store_true', dest='split_file')


def main():
    """Main command."""
    args = parser.parse_args()
    print(args)
    outline(args.infile, args.levels, args.split_file)


if __name__ == '__main__':
    main()
