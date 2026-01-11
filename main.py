# Array that contains all NATO Phonetic Alphabet strings.
nato_alphabet = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf",
                 "Hotel", "India", "Juliet", "Kilo", "Lima", "Mike", "November",
                 "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform",
                 "Victor", "Whiskey", "X-Ray", "Yankee", "Zulu"]

# TODO: Account for numbers/integers
input_string = input("Enter the text you need to have it converted into the NATO Phonetic Alphabet!\n").upper()

def convert_to_nato(char: str):
    """
    Find the corresponding NATO string value in the array based on its index
    after subtracting its ASCII value from the starting point of 65 (which is 'A').
    """
    return nato_alphabet[ord(char) - 65]

i = 0

# FIX: Output is buggy in terminal
for letter in input_string:
    if letter.isdigit():
        print(letter, end=", ")
        if i != len(input_string) - 1:
            print(letter)
    else:
        if i != len(input_string) - 1:
            print(convert_to_nato(letter), end=", ")
        else:
            print(convert_to_nato(letter))
    i += 1
