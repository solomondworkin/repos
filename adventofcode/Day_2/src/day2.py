

def solution_part_one():

    inpt = open("input", "r")

    lines = inpt.readlines()
    word_counter = 0

    for line in lines:
        policy = line.split(":")[0]
        password = line.split(":")[1].strip()
        min = policy.split("-")[0]       
        max_1 = policy.split("-")[1]
        max = max_1.split()[0]
        letter = max_1.split()[1]
        
        letter_counter = 0
        for i in password:
            if i == letter:
                letter_counter +=1
        if (letter_counter <= int(max)) and (letter_counter >= int(min)):
            word_counter += 1




    print(word_counter)


def solution_part_two():

    inpt = open("input", "r")

    lines = inpt.readlines()
    word_counter = 0

    for line in lines:
         policy = line.split(":")[0]
         password = line.split(":")[1].strip()
         position1 = policy.split("-")[0]
         other = policy.split("-")[1]
         position2 = other.split()[0]
         letter = other.split()[1]

         if (password[int(position1)-1] == letter) and (password[int(position2)-1] != letter):
             word_counter += 1
         if (password[int(position1)-1] != letter) and (password[int(position2)-1] == letter):
             word_counter += 1

    print(word_counter)


solution_part_one()

solution_part_two()




