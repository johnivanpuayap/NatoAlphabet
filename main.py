import pandas as pd

# Open the file and create the Dictionary
data = pd.read_csv("Day 26/Nato Alphabet/nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# Ask for input
inputted_words = input("Enter a word: ").upper()

# Create a list of Code Words
result = [data_dict[letter] for letter in inputted_words]
print(result)