import sys

def get_string(number, i, base="decimal"):
    if base == "decimal":
        number2 = len(str(i))
        curr_str = str(i)
    elif base == "octal":
        number2 = len(str(oct(i)))-2
        curr_str = oct(i)[2:]
    elif base == "hexadecimal":
        number2 = len(str(hex(i)))-2
        curr_str = hex(i)[2:].upper()
    elif base == "binary":
        number2 = len(str(bin(i)))-2
        curr_str = bin(i)[2:]
    else:
        raise Exception("The base '{0}' is not recognized. The other values are number = '{1}' and i = '{2}'.".format(base, number, i))
    return (' ' * (number - number2)) + curr_str

if (len(sys.argv) < 2):
    print("Usage: python baseConversions.py NUMBER_TO_PRINT_TO")
else:
    n = int(sys.argv[1])
    maxFormattingSize = len(bin(n))-1
    spacesInHeader = ' ' * (maxFormattingSize - 3)
    print("{0}DEC{1}BIN{2}OCT{3}HEX".format(spacesInHeader, spacesInHeader, spacesInHeader, spacesInHeader))
    for index in range (1, n+1):
        print(get_string(maxFormattingSize, index), end='')
        print(get_string(maxFormattingSize, index, "binary"), end='')
        print(get_string(maxFormattingSize, index, "octal"), end='')
        print(get_string(maxFormattingSize, index, "hexadecimal"))
