# This program help you find synonims or antonyms in case you need them
# This is powered by the datamuse API

import requests

base_url = 'https://api.datamuse.com/words'

def user_input():
    """Returns a word entered by the user as a string."""
    correct_input = False
    while not correct_input:
        word = input('\nEnter a word to search for:\n')
        if not word.isalpha():
            print('All characters must be letters. Try again.')
        else:
            correct_input = True
    return word


def list_of_words(word, selection, base_url=base_url):
    """Returns a list of 5 words, synonims , antonyms or 
    word with similar meaning, depending on the selection"""
    query_dict = dict()
    if selection == 1:
        query_dict['rel_syn'] = word
        query_dict['max'] = 5
    elif selection == 2:
        query_dict['rel_ant'] = word
        query_dict['max'] = 5
    elif selection == 3:
        query_dict['ml'] = word
        query_dict['max'] = 5
    response = requests.get(base_url, params=query_dict)
    data = response.json()
    words = [d['word'] for d in data]
    if len(words) < 1:
        return None
    return words

def main():
    print('''
    What do you want to do?
    Please, select an option form the menu below.
    
    (1) Find synonims of a word
    (2) Find antonyms of a word
    (3) Find word woth similar meaning to mine
    (0) Exit
    ''')
    
    valid_selection = False
    while not valid_selection:
        selection = input('Enter selection:\n')
        try:
            selection = int(selection)
            if selection >= 0 and selection <= 3: # Can be updated if program grows
                valid_selection = True
            else:
                print('\nInvalid selection')
        except:
            print('\nPlease enter number.')
    
    if selection == 0:
        exit()
    
    elif selection == 1:
        word = user_input()
        syns = list_of_words(word, selection)
        if syns is None:
            print(f'No synonims for "{word}" were found!')
        else:
            synonims_list = enumerate(syns, start=1)
            print()
            for number, synonim in synonims_list:
                print(f'{number}. {synonim}')

    elif selection == 2:
        word = user_input()
        ants = list_of_words(word, selection)
        if ants is None:
            print(f'No antonyms for "{word}" were found!')
        else:
            antonyms_list = enumerate(ants, start=1)
            print()
            for number, antonym in antonyms_list:
                print(f'{number}. {antonym}')

    elif selection == 3:
        word = user_input()
        sims = list_of_words(word, selection)
        if sims is None:
            print(f'No similar words for "{word}" were found!')
        else:
            similars_list = enumerate(sims, start=1)
            print()
            for number, similar in similars_list:
                print(f'{number}. {similar}')


if __name__ == '__main__':
    main()