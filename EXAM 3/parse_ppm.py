# ---------------------------------------------------------------------------------------------------------------
# Kristi LaVigne
# CSCI 236
# 04/12/2021
# Program Exam 3 - PPM files
# hours: 5
# Grade Version - n/a
# major problems: doesn't write a file or give any of the messages, no error given when compiling
# status of the program: doesn't function properly
# ---------------------------------------------------------------------------------------------------------------
"""
 KD Nuggets link provided states that it is taking in and manipulating JPEGs
 Most of the documentation and examples that I can find for ppm manipulation is for P3,
 this is portions of code written by shivinkapur and modified by me for PPM P3
 https://github.com/shivinkapur/functionalProgramming/blob/48bfa417385af5a9925423aafe7eb015b421cda5/Homeworks/Homework%204/hw4soln.py
 This does not work because the it throws an invalid syntax error, most likely because of the version differences
"""
# import packages
import struct
import sys


# parse the file named fname into a dictionary of the form
# {'width': int, 'height' : int, 'max' : int, 'pixels' : (int * int * int) list}
def parse_ppm(fname):
    ppm = {}
    f = open(fname, "rb")
    p6 = f.readline()
    dimensions = f.readline().split()
    ppm['width'] = int(dimensions[0])
    ppm['height'] = int(dimensions[1])
    ppm['max'] = int(f.readline())

    pixels = []
    rgb_b = f.read(3)
    while rgb_b != "":
        # we're assuming that the max val is less than 256
        # hence each pixel value fits in a single byte
        # for greater than 256, 2 bytes are used
        pixels.append(struct.unpack('BBB', rgb_b))
        rgb_b = f.read(3)
    ppm['pixels'] = pixels
    f.close()
    return ppm


# write the given ppm dictionary as a PPM image file named fname
# the function should not return anything
def un_parse_ppm(ppm, fname):
    f = open(fname, "wb")
    f.write("P6\n")
    f.write(str(ppm['width']) + " " + str(ppm['height']) + "\n")
    f.write(str(ppm['max']) + "\n")
    pixels = [struct.pack('BBB', p[0], p[1], p[2]) for p in ppm['pixels']]
    f.writelines(pixels)
    f.close()


# produce a greyscale version of the given ppm dictionary.
# the resulting dictionary should have the same format,
# except it will only have a single value for each pixel,
# rather than an RGB triple.
def grey_scale(ppm):
    pgm = ppm.copy()
    # map over the ppm pixels to create the pgm pixels!
    pgm['pixels'] = [int(round(.299 * rgb[0] + .587 * rgb[1] + .114 * rgb[2])) for rgb in ppm['pixels']]
    return pgm


# take a dictionary produced by the greyscale function and write it as a PGM image file named fname
# the function should not return anything
def un_parse_pgm(pgm, fname):
    w = pgm['width']
    h = pgm['height']
    m = pgm['max']
    l = pgm['pixels']
    with open(fname, 'w') as f:
        f.write("P6\n")
        f.write(str(w) + " " + str(h) + "\n")
        f.write(str(m) + "\n")
        for a in l:
            t = struct.pack('B', a)
            f.write(t)


def main():
    print("This program will convert a color ppm to greyscale.\n")
    file_in = sys.argv[1]
    file_out = sys.argv[2]
    print("arg 1: " + file_in + "\narg 2: " + file_out)

    input_file = open(file_in, 'r')
    grey_scale(input_file)
    print('Your ppm image has been converted to grayscale.\nThe output is in ' + file_out)

    if file_in == ' ' or file_out == ' ':
        print("INVALID COMMAND LINE ARGUMENTS")
        sys.exit()
    else:
        try:
            un_parse_ppm(un_parse_pgm(parse_ppm(file_in)), file_out)
            print('Your ppm image has been converted to grayscale.\nThe output is in ' + file_out)
        except IOError:
            print("Error: cannot read data or file not found ")
            sys.exit()
        else:
            print("INPUT FILE IS NOT A VALID PPM P6 FORMAT")
            sys.exit()


if __name__ == '__main__':
    main()
