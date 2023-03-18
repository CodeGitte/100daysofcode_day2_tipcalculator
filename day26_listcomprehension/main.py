#todo1: create dictionary 
import pandas as pd
df = pd.read_csv('nato_phonetic_alphabet.csv')
dict_nato = dict(zip(df.letter, df.code))
print(dict_nato)


#todo2. Create a list of the phonetic code words from a word that the user inputs
name = input("What is your name? ").upper()
phonetic_words = [dict_nato[letter] for letter in name]
print(phonetic_words)