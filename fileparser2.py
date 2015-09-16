# import sys
import os

######### WRITING FILE OUT #########
#open file to write
to_read_write_file_pointer = open('to_read.txt', 'w+')
#FOR: number in range from 1 to 10, write the number and a new line to our file.
for number in range(1, 10):
    #write number to file (with a new line)
    to_read_write_file_pointer.write("{0}\n".format(number))
#create a list of letters to output to file
letters = ['a', 'b', 'c', 'd', 'e']
#FOR: letter in letters from a to e, write letter and a new line to file
for letter in letters:
    #write letter to file (with a new line)
    to_read_write_file_pointer.write("{0}\n".format(letter))
#close file
to_read_write_file_pointer.seek(0)
output_file_pointer = open('output.txt', 'w')

######### READING FILE IN ##########
#FOR: line in to_read_file_pointer, read and print each line
for line in to_read_write_file_pointer:
    #print line
    output_file_pointer.write('Line: {0}'.format(line))
#close file
to_read_write_file_pointer.close()
output_file_pointer.close()
#ALL DONE
# os.remove('to_read.txt')
# raise SystemExit(0)

##Look into seek() for resetting file pointer in assignment to read/write files in a script