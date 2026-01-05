
import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#Loop through rows of a data frame
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:    
        output = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Invalid input. Only letters are allowed.")
        generate_phonetic()
    else:
        print(output)

generate_phonetic()
