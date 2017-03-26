

letter1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
letter2 = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'


input_file = "textfile.txt"
output_file = 'rot13_encoded.txt'



def rot13_encode(letter):
    try:
        number = letter1.index(letter)  # for example A index is on index 0 in letter1,
                                        # so the encoded letter will be
                                        # on the corresponding index in letter2 (letter2[0])
        encoded = letter2[number]
    except:                             # broad exception to catch numbers and spaces
        encoded = letter
    return encoded


def read_file_letters():
    outputfile = open(output_file, 'w')    # opening file to write the encoding
    with open(input_file, 'r') as file:
        for line in file:
            for letter in line:
                outputfile.write(rot13_encode(letter))
        outputfile.close()
    outputfile.close()

if __name__ == "__main__":

    read_file_letters()
