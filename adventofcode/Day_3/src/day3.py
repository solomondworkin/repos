

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


def line_search(x_move, y_move):

    inpt = open("input", "r")
    lines = inpt.readlines()
    line_number = 0
    column_number = 0

    while line_number < len(lines):
        




solution_part_one()

solution_part_two()


