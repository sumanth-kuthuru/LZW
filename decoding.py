# Name : Sumanth Kuthuru
# Student ID : 801166362

import struct
import sys

LZW_file = sys.argv[1]
file = open(LZW_file, "rb")           # Opens the previously stored LZW file 
a = file.read()
file.close()
i= 0

input_codes = []                       
while i< len(a):
    b = a[i:i+2]
    c = struct.unpack('>H', b)          #this line outputs a tuple (val,) Format H is used
    input_codes.append(c[0])            #c[0] will give the values as we only need the values unpacked
    i=i+2
#print(input_codes)                     #prints the unpacked codes

bit_length = int(sys.argv[2])

if  bit_length <= 16 and bit_length >= 9:
    max_table_size = 2**bit_length
    table = [None]*256                  #takes 256th  value as none temporarily
    for i in range(0,256):              #gives ascii values to range of indexes
        table[i] = chr(i)
    decode_output = []                  #This is for storing the output after decoding
    current_string = ""                 
    current_string=table[input_codes[0]]
    decode_output.append(current_string)    #adds first element to the decomp_output
    new_string = ""

    for i in range(1,len(input_codes)):      #Checks for range in number of input_codes
        code = input_codes[i]               #If exists in the range, the code will be the same number    
        if code not in range(0, len(table)) :
            new_string = current_string + current_string[0]
    
        else:    
            new_string = table[code]
        decode_output.append(new_string)        #appends the new_string to the output
        if len(table) <= max_table_size:    
            table.append(str(current_string + new_string[0]))

        current_string = new_string
       # print(table)                        # prints the updated table
        text = ""
        for string in decode_output:
            text += string                   #combines all the strings to give output string
    print(text)

    file = open("input_decoded.txt", "w")           #creates a text file input_decoded.txt
    file.write(text)                                #writes the output to the text file
    file.close()
else:
    print ("length should be between 9 and 16 only")
    

    






