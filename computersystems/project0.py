# get file name
name = input("What is the name of your file?")

# get directory
directory = input("What is the directory called?")

# input directorylocation/<filename>.in
# current functionality: opens file, reads file, writes contents of file to output, removes empty spaces and
# single line output, saves output to output file

with open(directory+"/"+name+"a", "w") as output, open(directory+"/"+name,"r") as data:
    lines = data.readlines()
    comment = False
    # for loop iterates through each line in document
    for line in lines:
        l = line.split("//")
        l[0] = l[0].replace(" ", "")
        if len(l) > 1:
            l[0] += "\n"
        if len(l) == 0:
            l[0] = l[0].replace("\n","")
        character = 0
        begin_comment = "/*"
        end_comment = "*/"
        # while loop iterates through each character in each line
        while character < len(l[0]):
            # if it encounters the beginning of a comment, changes comment value to true
            if l[0][character:character+2] == begin_comment and comment == False:
                comment = True
                character += 1
            # if it encounters the end of a comment, changes the comment value to false
            elif l[0][character:character+2] == end_comment and comment == True:
                comment = False
                character += 1
            # if it encounters a character that is not white space, it writes the character
            elif comment == False and character != "\n" and character != "\t":
                output.write(l[0][character])
            character +=1
