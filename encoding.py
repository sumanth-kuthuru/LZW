# Name : Sumanth Kuthuru
# Student ID : 801166362

import struct
import sys

input_file = sys.argv[1]
file = open( input_file , "r")      #opens the input file
input_text = file.read()
file.close()                        


bit_length = int(sys.argv[2])       # Number of encoding bits is saved in bit length

if  bit_length <= 16 and bit_length >= 9:
    max_table_size = 2**bit_length
    encode_output = []              # This is an empty list which is used to store the encoded data
    table = []                       # initializing the table              
    for i in range(0,256):
        table.append(chr(i))            #char(i) will give ascii values of int i
        
    #print(table)                       # prints the table before updating


    current_string = ""                # currrent string is an empty list which will store the first
    for next_symbol in input_text :     # next_symbol reads all the characters in the input.txt file individually next symbol at every step
        new = current_string + next_symbol  # New combines both the strings 
        if new in table:
            current_string = new      # if exists in table, Current_string will be new and will be added to the table
        else:
            encode_output.append(table.index(current_string)) 
            if len(table) < max_table_size:         # checks if the table length is exceeded to max_table_size or not
                table.append(current_string + next_symbol)
            current_string = next_symbol
    encode_output.append(table.index(current_string))       
    #print(table)                               #prints the table after updating

    print(encode_output)                       # prints the output after encoding

    x = '>' + str(len(encode_output))+'H'       # The byte order used is big endian('>')

    file = open("input.lzw", "wb")          # opens new file in LZW file format

    file.write(struct.pack( x, *encode_output)) # writes the packed data into LZW file

    file.close()

  #  print(struct.calcsize(x))    #  prints value which is total no of bytes being stored in file input.lzw

    
    
else:
    print ("length should be between 9 and 16 only")
    
	