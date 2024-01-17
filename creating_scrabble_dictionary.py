import os
import csv

# scrabble score system in a python dictionary
score_system = {'a':1, 'b':3, 'c':3, 'd':2,'e':1, 'f':4, 'g':2,'h':4,'i':1, 'j':8, 'k':5, 'l':1, 'm':3, 'n':1, 'o':1, 'p':3, 'q':10, 'r':1, 's':1, 't':1, 'u':1, 'v':4, 'w':4, 'x':8, 'y':4, 'z':10}

def word_score(word):
    ''' This function calculates the scrabble word score of a given word (excluding any extra positional points e.g. triple word score)'''

    score = 0
    for letter in word.lower():
        try:
            score += score_system[letter]
        except:
            #removing any words with spaces, hyphens or other non-alphabetical characters
            continue
    
    return score


# creating system agnostic paths for the current folder and the 'word list in csv' folder within
current_folder = os.path.dirname(os.path.abspath(__file__))
words_folder = os.path.join(current_folder, 'word lists in csv')

# constructing a list of the file names in the word list folder (alphabetical order)
words_file_list = sorted(os.listdir(words_folder))

# creating a list which will accumulate the words across all of the (26) csv files
all_words_list = []

# this for loop iterates through each csv file in the 'word lists in csv' folder, adding each line of the files to the all_words_list list
for file in words_file_list:
    file_path = os.path.join(words_folder, file)
    with open(file_path, 'r', encoding='iso-8859-1') as file:
        reader = csv.reader(file)
        for row in reader:
            if row: # skips any empty rows
                word = row[0].strip()
                all_words_list.append(word)

# removing any repeat words
all_unique_words = sorted(list(set(all_words_list)))

# removing all errors in the given csv files of words. This includes multiple words, hyphenated words, and other non-alphabetic characters
all_scrabble_words = [word for word in all_unique_words if all(char.isalpha() for char in word)]

print(len(all_unique_words))
print(len(all_scrabble_words))


with open('scrabble_dictionary.csv', 'w') as file:
    writer_object = csv.writer(file)
    for word in all_scrabble_words:
        writer_object.writerow([word,word_score(word)])




print('done')


