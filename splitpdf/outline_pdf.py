"""Add description here."""
import types
from PyPDF2 import PdfFileReader


def level(levels, index):
    """Construct level."""
    temp = list(levels)
    temp.append(str(index))
    return temp


def outline_level(items, levels, ipdf):
    """Outline a level."""
    index = 0

    for item in items:

        if isinstance(item, types.ListType):
            outline_level(item, level(levels, index), ipdf)
        else:
            index += 1
            print('%s: %s - %s' %
                  ('.'.join(level(levels, index)), item.title, ipdf.getDestinationPageNumber(item) + 1))


def outline(infile='in.pdf'):
    """Fetch outline from pdf."""
    ipdf = PdfFileReader(open(infile, 'rb'))

    outline_level(ipdf.outlines, [], ipdf)
