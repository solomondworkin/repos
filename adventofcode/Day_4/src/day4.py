

def passports_separator():
    '''
    Output: A list of passports taken from the plaintext "input" file
    '''

    inpt = open("input", "r").read()
    passports = []
    string = ""
    end_passport = False

    # splits the text file into list of passports
    for char in inpt:
        
        # case that we have hit out second newline char in a row, passport end
        if char == "\n":
            if end_passport == True:
                passports.append(string)
                string = "" 

        # case that we may be approaching end of passport
        if end_passport == False and char == "\n":        
            string += " "
            end_passport = True

        # case that we have not hit a newline character
        if char != "\n":
            end_passport = False
            string += char

    passports.append(string)

    return passports

def passport_separator(passports):
    '''
        Input: A list of passports from the passports_separator function
        Output: A list of lists of valid passport elements
    '''
    
    cid_counter = 0
    passport_count = 0

    passport_element_list = []

    for passport in passports:
        passport_elements = passport.split()

        # This part of the function counts the number of valid passports in the list
        if len(passport_elements) == 8:
            passport_element_list.append(passport_elements)
            passport_count += 1

        if len(passport_elements) == 7:
            for field in passport_elements:
                if "cid" not in field:
                   cid_counter += 1

        if cid_counter == 7:
            passport_count += 1
            passport_element_list.append(passport_elements)
        cid_counter = 0 

    print("There are", passport_count, "passports with the correct fields.")
    return(passport_element_list)


def field_check(passport_elements):
    '''
        Input: A list of lists of passport elements
        Output: The number of passports for which each field is correct
    '''
    num_correct = 0

    hair_color = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    eye_color = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    for passport in passport_elements:
        correct_fields = 0
        print("new passport:")
        for field in passport:
            value = field.split(":")[1]
            key = field.split(":")[0]

            if key == "byr":
                year = int(value)
                if year > 1919 and year < 2003:
                    correct_fields += 1
                    print("in byr")
            if key == "iyr":
                year = int(value)
                if year > 2009 and year < 2021:
                    correct_fields += 1
                    print("in iyr")
            if key == "eyr":
                year = int(value)
                if year > 2019 and year < 2031:
                    correct_fields += 1
                    print("in eyr")
            if key == "hgt":
                if value[:-2].isdigit() == True: 
                    height = int(value[:-2])
                    if value[-2:] == "cm":
                        if height > 149 and height < 194:
                            correct_fields += 1
                            print("in hgt")
                    if value[-2:] == "in": 
                        if height > 58 and height < 77:
                            correct_fields += 1
                            print("in hgt")
            if key == "hcl":
                hair_counter = 0
                if value[0] == "#":
                    for i in value[1:]:
                        if i in hair_color:
                            hair_counter += 1
                if hair_counter == 6:
                    correct_fields += 1
                    print("in hcl")
            if key == "ecl":
                if value in eye_color:
                    correct_fields += 1
                    print("in ecl")
            if key == "pid":
                if len(value) == 9:
                    if value.isdigit() == True:
                        correct_fields += 1              
                        print("in pid")
            if key == "cid":
                correct_fields += 1
                print("in cid")
 #           print(correct_fields)
            if correct_fields == len(passport):
                num_correct += 1

            
    print(num_correct)


def solution_part_one():

    passports = passports_separator()
    passport_separator(passports)




def solution_part_two():

    passports = passports_separator()
    split_passports = passport_separator(passports)
    field_check(split_passports)






 

#solution_part_one()

solution_part_two()
