Bookifier
==========
An easy way to print bind-ready booklets, in order to make (actually assemble) books right in your desktop.
------------------------------------------------------------------------------------------------------------
The main goal is to be able to print books in a flexible an easy way. Currently, it supports:

- Creating a ready-to-print pdf with as many sheets per booklet as you want.
- Autofill with blank pages ir order to use any number of pages as input.

Usage
-----
bookifier --outfile output.pdf --infile input.pdf --start first_page --stop last_page --size sheets_per_booklet [--help]

TODO
----
Some things that I would like to implement soon are:
- Optional QT gui
- Merging of several files while bookifying

Dependencies
------------
- Python 3
- PyPDF2
