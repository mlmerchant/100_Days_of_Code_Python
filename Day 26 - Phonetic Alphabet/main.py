with open("nato_phonetic_alphabet.csv") as f:
    phonetics_list = f.read().split()[1:]

phonetics_list = [item.split(",") for item in phonetics_list]
phonetics_dict = {item[0]: item[1] for item in phonetics_list}

word = input("Enter a word: ")
word_in_phonetics = [phonetics_dict[x] for x in word.upper() if x.isalpha()]
print(word_in_phonetics)

