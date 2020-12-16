

def solution_part_one():
    '''
        Input: Map of trees on Toboggan slope
        Output: Number of trees when hit by certain path
    '''


    inpt = open("input", "r")
    lines = inpt.readlines()
    counter = 0
    output = 0
    not_in_first_line = False

    for line in lines:        

        line = line[:-1]

        if not_in_first_line == True:

            counter += 3

            while counter+1 > len(line):
                line += line

            if line[counter] == "#":
                output += 1
            print(len(line))


        not_in_first_line = True



    print(output)
    return(output)


def line_search(y_move, x_move):

    inpt = open("input", "r")
    lines = inpt.readlines()
    line_number = x_move
    column_number = y_move
    output = 0

    for line in lines:

        if line_number != lines.index(line):
            continue

        line = line[:-1]
        print(line)
        line_number += x_move
  
        while column_number+1 > len(line):
            line += line

        if line[column_number] == "#":
            output += 1    

        column_number += y_move

    print(output)
    return(output)


#solution_part_one()

print(line_search(1,1) * line_search(3,1) * line_search(5,1) * line_search(7,1) * line_search(1,2))

