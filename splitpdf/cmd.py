"""Parse arguments."""
import argparse
import re
import os

from split import split_pdf


def existing_file(str):
    """Check if str is an existing file."""
    if not os.path.isfile(str):
        raise argparse.ArgumentTypeError('%r must be an existing file' % str)

    return str


def non_existing_file_or_diir(str, default_name='out.pdf'):
    """Check if str is a directory or non-existing file."""
    if os.path.isfile(str):
        raise argparse.ArgumentTypeError(
            '%r cannot refer to an existing file' % str)

    if os.path.isdir(str):
        return os.path.join(str, default_name)

    dirname = os.path.dirname(str)

    if dirname and not os.path.isdir(dirname):
        raise argparse.ArgumentTypeError(
            '%r must be valid directory' % dirname)

    return str


def number_or_range(str):
    """Check if str is number or a number range."""
    expr = re.match(r'^([1-9][0-9]*)(?:-([1-9][0-9]*|END))?$', str)
    if not expr:
        raise argparse.ArgumentTypeError(
            '%r must be either a number a range of two numbers' % str)

    range = {'start': int(expr.group(1))}

    if not expr.group(2):
        range['end'] = range['start']
    elif expr.group(2) != 'END':
        range['end'] = int(expr.group(2))
    else:
        range['end'] = 0

    if range['end'] and range['end'] < range['start']:
        raise argparse.ArgumentTypeError(
            'start must be equal or less than end: %s<=%s' % (range['start'], range['end']))

    return range


parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('--in', type=existing_file, dest='infile')
parser.add_argument('--out', type=non_existing_file_or_diir, dest='outfile')
parser.add_argument('--page', nargs='+', type=number_or_range, dest='pages')


def main():
    """Main command."""
    args = parser.parse_args()

    split_pdf(args.pages, args.infile, args.outfile)


if __name__ == '__main__':
    main()
