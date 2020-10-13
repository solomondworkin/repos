# get file name
name = input("What is the name of your file?")

#get directory
directory = input("What is the directory called?")

# input directorylocation/<filename>.in
# current functionality: opens file, reads file, writes contents of file to output, removes empty spaces and
# single line output, saves output to output file

with open(directory+"/"+name+"a", "w") as output, open(directory+"/"+name,"r") as data:
    lines = data.readlines()
    for line in lines:
        l = line.split("//")
        l[0] = l[0].replace(" ", "")
        if len(l) > 1:
            l[0] += "\n"
        if l[0].rstrip():
            output.write(l[0])
