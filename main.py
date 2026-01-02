# Array that contains all NATO Phonetic Alphabet strings.
nato_alphabet = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf",
                 "Hotel", "India", "Juliet", "Kilo", "Lima", "Mike", "November",
                 "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform"
                 "Victor", "Whiskey", "X-Ray", "Yankee", "Zulu"]

input_string = input("Enter the text you need to have it converted into the NATO Phonetic Alphabet!\n").upper()

# TODO: Account for numbers/integers
def convert_to_nato(char: str):
    """
    Match the provided uppercase character to its ASCII value and output its converted NATO value.
    """
    return nato_alphabet[ord(char) - 65]

for letter in input_string:
    print(convert_to_nato(letter))
