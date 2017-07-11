"""Add description here."""
import types
from PyPDF2 import PdfFileReader
from split import split_pdf


def level(levels, index):
    """Construct level."""
    temp = list(levels)
    temp.append(str(index))
    return temp


def outline_level(items, levels, ipdf, max_levels, stored_levels):
    """Outline a level."""
    index = 0

    if len(levels) == max_levels:
        return

    for item in items:

        if isinstance(item, types.ListType):
            outline_level(item, level(levels, index),
                          ipdf, max_levels, stored_levels)
        else:
            index += 1
            new_level = level(levels, index)
            stored_levels.append({
                'level': new_level,
                'title': item.title,
                'startAt': ipdf.getDestinationPageNumber(item) + 1
            })


def find_next(from_index, value_or_less, items):
    """Find next item that the specified outline level or less."""
    for i in xrange(from_index, len(items)):
        current = items[i]
        if len(current.get('level')) <= value_or_less:
            return i
    return -1


def outline(infile='in.pdf', levels=1, split=False):
    """Fetch outline from pdf."""
    ipdf = PdfFileReader(open(infile, 'rb'))

    saved_levels = []
    outline_level(ipdf.outlines, [], ipdf, levels, saved_levels)

    pages = ipdf.getNumPages()

    for i in xrange(0, len(saved_levels)):
        current = saved_levels[i]

        j = find_next(i + 1, len(current.get('level')), saved_levels)
        if j == -1:
            current['ends'] = pages
        else:
            current['ends'] = saved_levels[j].get('startAt') - 1

    if(split):
        for entry in saved_levels:
            file_name = 'chap-%s.pdf' % '-'.join(entry.get('level'))
            range = {'start': entry.get('startAt'), 'end': entry.get('ends')}

            split_pdf([range], infile, outfile=file_name)

    return saved_levels
