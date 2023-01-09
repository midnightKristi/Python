# ---------------------------------------------------------------------------------------------------------------
# Kristi LaVigne
# CSCI 236
# 04/12/2021
# Program Exam 3 - PPM files
# hours: 5
# Grade Version - n/a
# major problems: no error given when it compiles, doesn't write a file or give any of the messages
"""
         KD Nuggets link provided states that it is taking in and manipulating JPEGs
         Most of the documentation and examples that I can find for ppm manipulation is for P3
         These waerehelpful though:
             https://www.geeksforgeeks.org/python-pil-imageops-greyscale-method/
             https://pillow.readthedocs.io/en/3.0.x/reference/Image.html#PIL.Image.fromarray
"""
# status of the program: compiles without error but doesn't function properly
# ---------------------------------------------------------------------------------------------------------------

# import packages
import sys
import PIL
from PIL import Image, ImageOps
import numpy as np


def gray_scale(file_in, file_out):
    try:
        in_file = Image.open(file_in)
        gray_file = ImageOps.grayscale(in_file)
        gray_file.show()
        gray_file.save(file_out)

        in_file.close()
        gray_file.close()
    except IOError:
        print("ERROR CANNOT OPEN FILES")
        sys.exit()


def main():
    file_in = sys.argv[1]
    file_out = sys.argv[2]

    if file_in == ' ' or file_out == ' ':
        print("INVALID COMMAND LINE ARGUMENTS")
        sys.exit()

    if 'ppm' in file_in and 'ppm' in file_out:
        try:
            gray_scale(file_in, file_out)
            print('Your ppm image now is in grayscale.The output is in ' + file_out)
        except IOError:
            print("Error: cannot read data or file not found ")
            sys.exit()
    else:
        print("INPUT FILE IS NOT A VALID PPM P6 FORMAT")
        sys.exit()


if __name__ == '__main__':
    main()
