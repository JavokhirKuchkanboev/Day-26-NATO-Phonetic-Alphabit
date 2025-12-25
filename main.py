import pandas

names = pandas.read_csv("./nato_alphabet.csv")
names_dic = {row.Alphabet: row.Code for (index, row) in names.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        phonetic_list = [names_dic[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(phonetic_list)

generate_phonetic()



