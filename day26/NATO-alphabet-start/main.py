import pandas
#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# read file and turn DF into dict.
df_nato_phonetic_alphabets = pandas.read_csv('nato_phonetic_alphabet.csv')
dict_nato_phonetic_alphabets = {row.letter: row.code for (index, row) in df_nato_phonetic_alphabets.iterrows()}



#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
while True:
    # get user input
    input_word = input('Enter a word: ').upper()
    # make letters list from user name
    letters = [letter for letter in input_word]
    # output NATO phonetic alphabet on each letter
    try:
        for letter in letters:
            output_word = dict_nato_phonetic_alphabets[letter]
            print(f"{letter}: {output_word}")
        break
    except KeyError:
        print('Sorry, Only litters in the alphabet please')
        continue

