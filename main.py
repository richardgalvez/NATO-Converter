# Array that contains all NATO Phonetic Alphabet strings.
from typing import List


nato_alphabet = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf",
                 "Hotel", "India", "Juliet", "Kilo", "Lima", "Mike", "November",
                 "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform",
                 "Victor", "Whiskey", "X-Ray", "Yankee", "Zulu"]

input_string = input("Enter the text you need to have it converted into the NATO Phonetic Alphabet!\n")
output = []

def convert_to_nato(char: str):
    """
    Find the corresponding NATO string value in the array based on its index
    after subtracting its ASCII value from the starting point of 65 (which is 'A').
    """
    return nato_alphabet[ord(char) - 65]

def display_output(arr: List):
    i = 0

    for index in arr:
        if i != len(arr) - 1:
            print(index, end=", ")
        else:
            print(index)
        i += 1

# TODO: Handle special characters

for char in input_string:
    if char.isnumeric():
        output.append(str(char))
    elif char.isalpha():
        converted_char = convert_to_nato(char.upper())
        output.append(converted_char)

display_output(output)
