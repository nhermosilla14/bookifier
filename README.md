Bookifier
==========
An easy way to print bind-ready booklets, in order to make (actually assemble) books right in your desktop.
------------------------------------------------------------------------------------------------------------
The main goal is to be able to print books in a flexible and easy way. Currently, it supports:

- Creating a ready-to-print pdf with as many sheets per booklet as you want.
- Autofill with blank pages in order to use any number of pages as input.
- Does not require a duplex printer at all (and lets you print with a non borderless printer too, such as some Canon models as mine)

Usage
-----
bookifier --outfile output.pdf --infile input.pdf --start first_page --stop last_page --size sheets_per_booklet [--help]

Creating Brochure
-----------------
To make this works, do this:
- Fold all sheets by half (I highly recommend to use A4, since once folded it is A5)
- Put the sheets one by one in the printer tray (you can put them all at the same time, just not one inside the other)
- The explanation in case you didn't get it, goes now: Imagine you fold a single A4 sheet. You would get 4 printable pages, A-B on one side, C-D on the other. Now, the thing is this app will print A, then B, then C and D. So what you need to do is to print all A sides, then all B sides. After that fold inside out each sheet and print all C sides, and then all D sides. Remember to choose A5 as page size, and to scale properly, if necessary.

TODO
----
Some things that I would like to implement soon are:
- Optional QT gui
- Merging of several files while bookifying

Dependencies
------------
- Python 3
- PyPDF2
