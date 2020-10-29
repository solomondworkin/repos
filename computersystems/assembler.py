import sys

# Table of computation instructions:

comp = {
	"0" : "0101010", 
	"1" : "0111111",
    "-1" : "0111010",
    "D" : "0001100",
    "A" : "0110000",
    "M" : "1110000",
    "!D" : "0001101",
    "!A" : "0110001",
    "!M" : "1110001",
    "-D" : "0001111",
    "-A" : "0110011",
    "-M" : "1110011",
    "D+1" : "0011111",
    "A+1" : "0110111",
    "M+1" : "1110111",
    "D-1" : "0001110",
    "A-1" : "0110010",
    "M-1" : "1110010",
    "D+A" : "0000010",
    "D+M" : "1000010",
    "D-A" : "0010011",
    "D-M" : "1010011",
    "A-D" : "0000111",
    "M-D" : "1000111",
    "D&A" : "0000000",
    "D&M" : "1000000",
    "D|A" : "0010101",
    "D|M" : "1010101" 
}

# Table of destination instructions:

dest = {
	"null" : "000",
	"M" : "001",
	"D" : "010",
	"MD" : "011",
	"A" : "100",
	"AM" : "101",
	"AD" : "110",
	"AMD" : "111"
}

# Table of jump instructions:

jump = {
	"null" : "000",
	"JGT" : "001",
	"JEQ" : "010",
	"JGE" : "011",
	"JLT" : "100",
	"JNE" : "101",
	"JLE" : "110",
	"JMP" : "111"
}

# Table of symbols:

symbols = {
    "SP": 0,
    "LCL": 1,
    "ARG": 2,
    "THIS": 3,
    "THAT": 4,
    "SCREEN": 16384,
    "KBD": 24576,
    'R0': 0,
    'R1': 1,
    'R2': 2,
    'R3': 3,
    'R4': 4,
    'R5': 5,
    'R6': 6,
    'R7': 7,
    'R8': 8,
    'R9': 9,
    'R10': 10,
    'R11': 11,
    'R12': 12,
    'R13': 13,
    'R14': 14,
    'R15': 15,
}

'''
    This section is suppoed to remove whitespaces, comments, and trailing 
    lines from the file.
    Unfortunately, it doesn't work super well so we still have to .strip()
    and .rstrip() later. 
'''
name = sys.argv[1]

# reads the file and writes to the first intermediate file
with open("intermediate.asm", "w") as output, open(name,"r") as data:
    lines = data.readlines()
    comment = False
    only_comment = False
    # for loop iterates through each line in document
    for line in lines:
        # removes single line comments
        l = line.split("//")
        # removes blank spaces, tabs
        l[0] = l[0].replace(" ", "").replace("\t", "")
        # removes empty lines
        if len(l) > 1:
            l[0] += "\n"
        character = 0
        # indicates multi-line comment structure
        begin_comment = "/*"
        end_comment = "*/"

        # while loop iterates through each character in each line
        while character < len(l[0]):
            # if it encounters the beginning of a comment, changes comment value to true
            if l[0][character:character+2] == begin_comment and comment == False:
                comment = True
                # if the full line is a comment
                if character == 0:
                	only_comment = True
                character += 1
            # if it encounters the end of a comment, changes the comment value to false
            elif l[0][character:character+2] == end_comment and comment == True:
                comment = False
                if only_comment:
                	# move to next character if full line is a comment
                	character += 1
                	only_comment = False
                character += 1
            # if entire line is empty, move to next character
            elif character == 0 and l[0][character] == "\n":
                character += 1
            # if it encounters a character that is not white space, it writes the character
            elif comment == False:
                output.write(l[0][character])
            character +=1


#this names the output file
output = name[:-3] + "hack"
out = str(output)

# this deals with the variables
intermediate = open("intermediate.asm", 'r')
intermediate2 = open("intermediate2.asm", 'w')

'''
    This section passes through the cleaned .asm code, removing and 
    cataloging jump labels, and translating symbolic a-instructions
    to numbers.
'''

# this sets the number fo 
number = 0
free_address = 16
lines = intermediate.readlines()
for line in lines:

    # removes jump labels, catalogues them in symbol dictionary
    if "(" in line:
        intermediate = line.strip().rstrip()
        label = intermediate[1:-1].strip().rstrip()
        symbols[label] = number
        intermediate2.write("")
        # keeps line count consistent with output file lines
        number -=1
    number += 1

    # catalogues new variable names in symbol dictionary
    if "@" in line:
        # add all labels to symbols dictionary
        if line[1].isalpha() and line[1].islower():
            intermediate2.write(line)
            if line.partition("@")[2].strip().rstrip() not in symbols.keys():
                symbols[line.partition("@")[2].strip().rstrip()] = free_address
                free_address += 1
        if line[1].isnumeric():
            intermediate2.write(line)
        if line[1].isalpha and line[1].isupper():
            intermediate2.write(line)
    elif "(" not in line and "@" not in line:
        intermediate2.write(line)   
intermediate2.close()   


'''
    This section passes through the cleaned .asm code, removing and 
    cataloging jump labels, and translating symbolic a-instructions
    to numbers.
'''

finalopen = open("intermediate2.asm", 'r')
finalout = open(out,'w')
lines = finalopen.readlines() 

semicolon = ";"
equals = "="
for line in lines:
    if "@" in line:

        if line[1].isnumeric():
            finalout.write(str('{0:016b}'.format(int(line[1:]))) + "\n")

        if line[1].isalpha():
            key = line.partition("@")[2].strip().rstrip()
            finalout.write(str('{0:016b}'.format(symbols.get(key))) + "\n")
    else:
        newline = "111"
        #deal with comp instructions, when there is an = operator
        if equals in line:
            for key in comp:
                if key == line.partition(equals)[2].strip().rstrip():
                    newline += comp.get(key)
        #deal with comp instructions, when there is a ; operator
        if semicolon in line:
            for key in comp:
                if key == line.partition(semicolon)[0].strip().rstrip():
                	newline += comp.get(key)
        #deal with dest instructions
        if equals in line:
            for key in dest:
                if key == line.partition(equals)[0].strip().rstrip():
                    newline += dest.get(key)
        #if there is no destination, write in 0's
        if equals not in line:
            newline += "000"
        #deal with jump instructions
        if semicolon in line:
            for key in jump:
                if key == line.partition(semicolon)[2].strip().rstrip():
                    newline += jump.get(key)
        if semicolon not in line:
            newline += "000"        
        #write lines to new .asm file
        finalout.write(newline + "\n")





