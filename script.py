import os 
import csv

#user_input = input('Please input your set of letters (no separations)')


''' Each line of the csv file has two elements: the first is a word, and the second is its scrabble word score.
    To make the access of word scores easier, below I'll make a python dictionary with the keys as words, and their 
    corresponding values as the word scores. '''
scrabble_dictionary = {}

current_folder = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(current_folder, 'scrabble_dictionary.csv'), 'r') as file:
    reader_obj = csv.reader(file)

    for row in reader_obj:
        key,value = row
        scrabble_dictionary[key] = int(value)



def available_words(list_of_letters):
    ''' This function accepts a list (or any other iterable) of letters, and returns a list with all of 
        the possible words formed from those letters. '''
    
    final_list = []

    list = [word for word in scrabble_dictionary.keys()]
    
    # This for loop updates the final_list list, which aims to consist of words only with the inputted letters
    # The longest word in the dictionary is 21 letters. Hence, numbers 0-20 are needed to index every possible word
    for i in range(21):
        list = [word for word in list if word[i] in list_of_letters]
        final_list += [word for word in list if len(word) == i+1]
        list = [word for word in list if len(word) != i+1]


    # The following code removes words from the final_list list that have several occurrences of the same letter which the user's
    # list doesn't have

    final_list = [word for word in final_list if len(word) <= len(list_of_letters)]

    # dictionary with keys as unique letters in inputted list, and values as the count in the list
    letter_count = {}

    for letter in list_of_letters:
        letter_count[letter] = letter_count.get(letter, 0) + 1

    for key, value in letter_count.items():
        final_list = [word for word in final_list if word.count(key) <= value]
                

    return final_list


def scrabble_cheat_list(list_of_letters):
    ''' This function accepts a list (or any other iterable) of letters and returns a list of tuples 
        with the first elements being all of the possible words formed from those letters, and the second element
        being the corresponding scrabble word score.'''
    
    list_of_words = available_words(list_of_letters)
    return sorted([(word, scrabble_dictionary[word]) for word in list_of_words], key = lambda i:i[1], reverse=True)



#print(scrabble_cheat_list(['a','o', 'e', 't', 's', 'v', 'b']))
#print('\n'.join(scrabble_cheat_list(['a','o', 'e', 't', 's', 'v', 'b'])))


a = scrabble_cheat_list(['e', 'a', 's', 'p', 't', 'i', 'h', 'l'])
b = [f'{tupl[0]}: {tupl[1]}' for tupl in a]

print(b)




