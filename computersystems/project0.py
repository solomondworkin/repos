# get file name
name = input("What is the name and location of your file?")

# make output name
output = name[:-3] + ".out"

# reads the file and writes to the output file
with open(output, "w") as output, open(name,"r") as data:
    lines = data.readlines()
    comment = False
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
                character += 2
            # if it encounters the end of a comment, changes the comment value to false
            elif l[0][character:character+2] == end_comment and comment == True:
                comment = False
                character += 2
            # if entire line is empty, move to next character
            elif character == 0 and l[0][character] == "\n":
                character += 1
            # if it encounters a character that is not white space, it writes the character
            elif comment == False:
                output.write(l[0][character])
            character +=1
