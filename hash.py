# File: hash.py
# Zachary Muranaka
# Hash function that returns 10 "random" digits

def get_position_in_alphabet(char):
    if char == 'a':
        return 1
    elif char == 'b':
        return 2
    elif char == 'c':
        return 3
    elif char == 'd':
        return 4
    elif char == 'e':
        return 5
    elif char == 'f':
        return 6
    elif char == 'g':
        return 7
    elif char == 'h':
        return 8
    elif char == 'i':
        return 9
    elif char == 'j':
        return 10
    elif char == 'k':
        return 11
    elif char == 'l':
        return 12
    elif char == 'm':
        return 13
    elif char == 'n':
        return 14
    elif char == 'o':
        return 15
    elif char == 'p':
        return 16
    elif char == 'q':
        return 17
    elif char == 'r':
        return 18
    elif char == 's':
        return 19
    elif char == 't':
        return 20
    elif char == 'u':
        return 21
    elif char == 'v':
        return 22
    elif char == 'w':
        return 23
    elif char == 'x':
        return 24
    elif char == 'y':
        return 25
    elif char == 'z':
        return 26
    else:
        return -1

def get_ten_random_digits(word):
    str_num = ''

    for letter in word:
        str_num += str(get_position_in_alphabet(letter))

    num = (int(str_num) ** 7) * 17

    while len(str(num)) < 31:
        num *= int(str(num)[len(str(num))-1]) + 2

    str_num = str(num)[13:29]
    num = (int(str_num) - 3750347) * 11
    str_num = str(num)[3:]

    for i in range(len(str_num)):
        curr_digit = int(str_num[i])
        if curr_digit % 2:
            str_num = f"{str_num[:i]}{curr_digit-1}{str_num[i+1:]}"
        else:
            str_num = f"{str_num[:i]}{int(curr_digit/2)}{str_num[i+1:]}"

    num = int(str_num) ** 31
    while len(str(num)) < 51:
        num *= int(str(num)[len(str(num))-1]) + 3

    str_num = str(num)[17:41] + str(num)[7:13]
    num = (((((int(str_num) + 8340317) % 6998767) * 4025249) % 9533351) * 9137287) + 7423343

    while not num % 2:
        num /= 2

    str_num = str(int(num))[2:len(str(int(num)))-2]
    if not str_num[0]:
        num = int(str_num) * 919
    else:
        num = int(str_num) * 5581

    num = ((int(str_num) + 82567) * 47) + 134851
    str_num = str(int(num))[3:len(str(int(num)))-3]

    for digit in str_num:
        num += ord(digit)

    for digit in str_num:
        num *= ord(digit)

    num = ((int(str_num) + 9815557) * 8115761) ** 6277
    str_num = str(num)[29:1181]
    return [
        int(str_num[691]),
        int(str_num[19]),
        int(str_num[1003]),
        int(str_num[607]),
        int(str_num[811]),
        int(str_num[201]),
        int(str_num[486]),
        int(str_num[44]),
        int(str_num[223]),
        int(str_num[1114])
    ]

input_word = input("Enter a word (all lowercase, no spaces): ")
print(get_ten_random_digits(input_word))
