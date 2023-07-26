import pandas as pd

# Open the file and create a Dictionary
data = pd.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(data_dict)

# Ask for input


# Create a list of Code Words
while True:
    inputted_words = input("Enter a word: ").upper()

    try:
        result = [data_dict[letter] for letter in inputted_words]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
    else:
        print(result)
        break
