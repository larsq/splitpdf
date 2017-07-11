"""Module for pdf operations."""
from PyPDF2 import PdfFileWriter, PdfFileReader


def split_pdf(ranges, infile='in.pdf', outfile='out.pdf'):
    """Split pdf file."""
    ipdf = PdfFileReader(open(infile, 'rb'))
    all = PdfFileWriter()

    for range in ranges:
        start = range['start'] - 1
        endExclusive = range['end'] or ipdf.getNumPages()
        for i in xrange(start, endExclusive):
            all.addPage(ipdf.getPage(i))

    with open(outfile, 'wb') as f:
        all.write(f)
