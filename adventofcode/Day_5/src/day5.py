def id_list():
    '''
        Input: plaintext file "input" containing boarding passes separated by new line characters
        Output: list of boarding pass strings
    '''

    passes = open("input", "r")
    list_passes = passes.readlines()
    output = []

    for bpass in list_passes:
        output.append(bpass[:-1])
 
#    print(output)
    return output

def row_number(list_passes):
    '''
        Input: list of boarding passes separated by strings
        Output: row number of each boarding pass
    '''
    output = []

    for bpass in list_passes:
        top = 127
        bottom = 0
        for char in bpass[:7]:
            if char == "F":
                top = bottom + int((top-bottom)/2)
            if char == "B":
                bottom = top - int((top-bottom)/2)
        output.append(top)


    return output

def column_number(list_passes):
    '''
        Input: list of boarding passes separated by strings
        Output: column number of each boarding pass
    '''
    output = []

    for bpass in list_passes:
        top = 7
        bottom = 0
        for char in bpass[7:10]:
            if char == "L":
                top = bottom + int((top-bottom)/2)
            if char == "R":
                bottom = top - int((top-bottom)/2)
        output.append(top)


    return output



def seat_id(row, column):
    '''
        Input: two lists:  row numbers and column numbers for each boarding pass
        Output: seat ID of each boarding pass

    '''
    output = []
    i = 0
    
    while i < len(row):
        seat_number = (row[i]*8) + column[i]
        output.append(seat_number)
        i += 1

    return output


def seats_taken(rows, columns):

    row_dictionary = {}
    column_dictionary = {}

    for row in rows:
        if row in row_dictionary:
            row_dictionary[row] = row_dictionary[row] + 1
        if row not in row_dictionary:
            row_dictionary[row] = 1

    for column in columns:
        if column in column_dictionary:
            column_dictionary[column] = column_dictionary[column] + 1
        if column not in column_dictionary:
            column_dictionary[column] = 1

    return row_dictionary, column_dictionary



def solution_part_one():

    list_ids = id_list()
    rows = row_number(list_ids)
    columns = column_number(list_ids)
    seat_ids = seat_id(rows, columns)
    seat_ids.sort()
    print(seat_ids[-1])


def solution_part_two():

    list_ids = id_list()
    rows = row_number(list_ids)
    columns = column_number(list_ids)

    dict_rows, dict_columns = seats_taken(rows, columns)
    
    row_answer = min(dict_rows, key = dict_rows.get)
    column_answer = min(dict_columns, key = dict_columns.get)

    for i in dict_rows:
        print(dict_rows.get(i), i)

    for i in dict_columns:
        print(dict_columns.get(i), i)

    print(row_answer * 8 + column_answer)                



#solution_part_one()

solution_part_two()
