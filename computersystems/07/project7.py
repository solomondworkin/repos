import sys, os


'''
    This removes comments, and trailing lines from the .vm file.
'''

filename = sys.argv[1]

# reads the file and writes to the first intermediate file
with open("intermediate", "w") as output, open(filename,"r") as data:
    lines = data.readlines()
    comment = False
    only_comment = False
    # for loop iterates through each line in document
    for line in lines:
        # removes single line comments
        l = line.split("//")
        # removes blank spaces, tabs
        l[0] = l[0].replace("\t", "")
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


'''
    This translates the cleaned .vm file into a .hack file.
'''

input_file = open("intermediate", "r")
output_name = filename[:-2] + "asm"
output_file = open(output_name, "w")
#output_file = open("output.asm", "w")
lines = input_file.readlines()

# Arithmetic stuff
i = 0
arithmetic = ["add", "sub", "neg", "and", "not", "eq", "gt", "lt", "or"]
push = ["local", "argument", "this", "that", "static", "temp", "pointer", "constant"]

text = ""

for line in lines:

    # this translates arithmetic instructions    
    for key in arithmetic:  
        if key in line:

            if key == "add":
                text += "@SP\nAM=M-1\nD=M\n@SP\nAM=M-1\nM=D+M\n@SP\nM=M+1\n"
            if key == "sub":
                text += "@SP\nAM=M-1\nD=M\n@SP\nAM=M-1\nM=M-D\n@SP\nM=M+1\n"
            if key == "neg":
                text += "@SP\nA=M-1\nM=-M\n"
            if key ==  "and":
                text += "@SP\nAM=M-1\nD=M\n@SP\nA=M-1\nM=D|M\n"
            if key == "not":
                text += "@SP\nA=M-1\nM=!M\n"
            if key == "eq":
                text += "@SP\nAM=M-1\nD=M\n@SP\nA=M-1\nD=M\n@SP\nA=M-1\nD=M-D\nM=-1\n@CONTINUE" + str(i) + "\nD;JEQ\n@SP\nA=M-1\nM=0\n(CONTINUE" + str(i) + ")\n"
                i += 1
            if key == "gt":
                text += "@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\n@FALSE\nD;JLE\n@SP\nA=M-1\nM=-1\n@CONTINUE" + str(i) + "\n0;JMP\n(FALSE)\n@SP\nA=M-1\nM=0\n(CONTINUE" + str(i) + ")\n"
                i += 1
            if key == "lt":
                text += "@SP\nAM=M-1\nD=M\nA=A-1\nD=M-D\n@FALSE\nD;JGT\n@SP\nA=M-1\nM=-1\n@CONTINUE" + str(i) + "\n0;JMP\n(FALSE)\n@SP\nA=M-1\nM=0\n(CONTINUE" + str(i) + ")\n"
                i += 1
            if key == "or":
                text += "@SP\nA=M-1\nD=M\n@SP\nA=M-1\nM=D|M\n"

    # this translates push instructions
    if "push" in line:

        segment = line.split()[1]
        index = line.split()[2]
        if segment == "constant":
            text += "@" + index + "\nD=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        if segment == "local":
            text += "@LCL\nD=M\n@" + index + "\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        if segment == "argument":
            text += "@ARG\nD=M\n@" + index + "\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        if segment == "this":
            text += "@" + index + "\nD=A\n@THIS\nA=M+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        if segment == "that":
            text +=  "@" + index + "\nD=A\n@THAT\nA=M+D\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        if segment == "temp":
            text += "@5\nD=A\n@" + index + "\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        if segment == "pointer":
            text += "@3\nD=A\n@" + index + "\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"
        if segment == "static":
            text += "@" + filename[:-2] + index + "\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n"

    # this translates pop instructions
    if "pop" in line:

        segment = line.split()[1]
        index = line.split()[2]
        if segment == "local":
            text += "@LCL\nD=M\n@" + index + "\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n"
        if segment == "argument":
            text += "@ARG\nD=M\n@" + index + "\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n"
        if segment == "this":
            text += "@THIS\nD=M\n@" + index + "\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n"
        if segment == "that":
            text += "@THAT\nD=M\n@" + index + "\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n"
        if segment == "temp":
            text += "@5\nD=A\n@" + index + "\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n"
        if segment == "pointer":
            text += "@3\nD=A\n@" + index + "\nD=D+A\n@R13\nM=D\n@SP\nAM=M-1\nD=M\n@R13\nA=M\nM=D\n"
        if segment == "static":
            text += "@SP\nAM=M-1\nD=M\n@" + filename[:-2] + index + "\nM=D\nD"

      
output_file.write(text)
os.remove("intermediate")



