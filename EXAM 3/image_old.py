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
"""
# status of the program: compiles without error but doesn't function properly
# ---------------------------------------------------------------------------------------------------------------

# import packages
import sys


def gray_scale(file_in, file_out):
    try:
        in_file = open(file_in, 'r')
        gray_file = open(file_out, 'w')
    except IOError:
        print("ERROR CANNOT OPEN FILES")
        sys.exit()
    else:
        for x in range(0, 3):
            gray_file.write(in_file.readline())
        for line in in_file.readlines():
            linesplit = line.split()
            for word in range(0, len(linesplit), 3):
                mean = (int(linesplit[word]) + int(linesplit[word + 1]) + int(linesplit[word + 2])) / 3
                for i in range(0, 3):
                    linesplit[word + i] = int(mean)
                    gray_file.write(str(linesplit[word + i]))
                    gray_file.write(' ')
            gray_file.write('\n')
        in_file.close()
        gray_file.close()


def main():
    file_in = sys.argv[1]
    file_out = sys.argv[2]

    if file_in == ' ' or file_out == ' ':
        print("INVALID COMMAND LINE ARGUMENTS")
        sys.exit()

    if 'ppm' in file_in and 'ppm' in file_out:
        try:
            input_file = open(file_in, 'r')
            gray_scale(input_file, file_out)
            print('Your ppm image now is in grayscale.The output is in ' + file_out)
        except IOError:
            print("Error: cannot read data or file not found ")
            sys.exit()
    else:
        print("INPUT FILE IS NOT A VALID PPM P6 FORMAT")
        sys.exit()
