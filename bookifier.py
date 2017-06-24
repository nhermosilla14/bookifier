#!/usr/bin/env python3

from PyPDF2 import PdfFileReader, PdfFileWriter
import sys

def GetPagesToPrint(start, end, SHEETS_PER_BOOKLET):
    pages = list()
    if (end < start):
        print("Incorrect order. End must be greater than start! Exiting...")
        exit(-1)
    elif ((end - start + 1) % SHEETS_PER_BOOKLET * 4 != 0):
        blank_pages = (SHEETS_PER_BOOKLET * 4) - ((end - start + 1) % (SHEETS_PER_BOOKLET * 4))
        pages = list(range(start,end + 1))
        for i in range(blank_pages):
            pages.append(0)
    else:
        pages = list(range(start,end + 1)) 
    return pages

def GetFirstBatch(pages):
    batch = list()
    numpages = int(len(pages)/2)
    printable = range(0, numpages - 1, 2)
    for i in printable:
        batch.append(pages[i])
    return batch

def GetSecondBatch(pages):
    batch = list()
    numpages = int(len(pages)/2)
    printable = range(numpages * 2 - 1, numpages, -2)
    for i in printable:
        batch.append(pages[i])
    return batch

def GetThirdBatch(pages):
    batch = list()
    numpages = int(len(pages)/2)
    printable = range(1, numpages, 2)
    for i in printable:
        batch.append(pages[i])
    return batch

def GetFourthBatch(pages):
    batch = list()
    numpages = int(len(pages)/2)
    printable = range(numpages * 2 - 2, numpages - 1, -2)
    for i in printable:
        batch.append(pages[i])
    return batch

def ParseArguments(arguments):
    args = dict()
    if (len(arguments) == 1 or len(arguments) > 11):
        print("Tool to print easily-bindable books. \nUsage: bookifier --outfile output.pdf --infile input.pdf --start first_page --stop last_page --size sheets_per_booklet [--help]")
        return(args)
    else:
        for element in arguments:
            if (element == "--infile"):
                args['input_stream'] = arguments[arguments.index(element)+1]
            elif (element == "--outfile"):
                args['output_file'] = arguments[arguments.index(element)+1]
            elif (element == "--start"):
                args['first_page'] = int(arguments[arguments.index(element)+1])
            elif (element == "--end"):
                args['last_page'] = int(arguments[arguments.index(element)+1])
            elif (element == "--size"):
                args['size'] = int(arguments[arguments.index(element)+1])
            elif (element == "--help"):
                print("Tool to print easily-bindable books. \nUsage: bookifier --outfile output.pdf --infile input.pdf --start first_page --stop last_page --size sheets_per_booklet [--help]")
                return dict()
            else:
                pass
    return args


def main():
    printer = PdfFileWriter()
    arguments = ParseArguments(sys.argv)
    if len(arguments) == 0:
        exit(-1)
    input_stream = open(arguments['input_stream'], 'rb')
    output_file = open(arguments['output_file'], 'wb')
    first_page = arguments['first_page']
    last_page = arguments['last_page']
    SHEETS_PER_BOOKLET = arguments['size']
    input_file = PdfFileReader(input_stream)
    booklets = list()
    num_of_pages = last_page - first_page + 1
    if (num_of_pages % (4 * SHEETS_PER_BOOKLET)):
        num_of_pages +=  SHEETS_PER_BOOKLET * 4 - (num_of_pages % (4 * SHEETS_PER_BOOKLET))
    num_of_booklets = int(num_of_pages / (SHEETS_PER_BOOKLET * 4))
    print("Booklets: " + str(num_of_booklets))
    cur_booklet_page = first_page
    for i in range(num_of_booklets):
        pages = GetPagesToPrint(cur_booklet_page, cur_booklet_page + (4 * SHEETS_PER_BOOKLET) - 1, SHEETS_PER_BOOKLET)
        booklets.append(pages)
        cur_booklet_page = cur_booklet_page + 4 * SHEETS_PER_BOOKLET
    for booklet in booklets:
        batch = GetFirstBatch(booklet)
        for i in batch:
            if (i in range(first_page, last_page + 1)):
                printer.addPage(input_file.getPage(i-1))
            else:
                printer.addBlankPage()
        batch = GetSecondBatch(booklet)
        for i in batch:
            if (i in range(first_page, last_page + 1)):
                printer.addPage(input_file.getPage(i-1))
            else:
                printer.addBlankPage()
        batch = GetThirdBatch(booklet)
        for i in batch:
            if (i in range(first_page, last_page + 1)):
                printer.addPage(input_file.getPage(i-1))
            else:
                printer.addBlankPage()
        batch = GetFourthBatch(booklet)
        for i in batch:
            if (i in range(first_page, last_page + 1)):
                printer.addPage(input_file.getPage(i-1))
            else:
                printer.addBlankPage()
    printer.write(output_file)
    output_file.close()
    input_stream.close()
    return(0)

if __name__ == "__main__":
    main()

