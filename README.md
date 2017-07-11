Split PDF
=========
Extract pages from PDF file

WHAT
----
These scripts solves the case to:
1) Read the outline from a PDF file
2) Create individual files for each level

WHY
---
These scripts resembles about what PDFTK can do but is far easier
and solves the need for split a PDF into files that corresponds to
the outline level. There are probably other tools but the ones that
I have found is either too complex or too simple

Writing the few lines of codes to get the perfect tool was far simpler
than to find any good match amongst zillions of projects

INSTALLATION
------------
To be defined

Furter development
-------------------
- Cleanup of the code
- Making it easier to install


ISSUES
------
&#x2610; Optimize page ranges to avoid overlapping pages  
This can be achieved by sorting the range by start page and
keep a counter for the last page
