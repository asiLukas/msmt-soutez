
def scrabble(file, letters):
    valid_words = []
    # vytvoreni seznamu ze slov zadanych v souboru
    words = []
    with open(file, 'r') as f:
        for word in f.readlines():
            # pridam slovo do seznamu a odendam z neho novy radek
            words.append(word.strip())

    for word in range(len(words)):
        # docasne promenne pro resetovani po kazde iteraci
        curr_word = ''
        letters_temp = letters

        # loop skrz slovo pro jednotlive pismena
        for letter in range(len(words[word])):
            if words[word][letter] in letters_temp:
                # pokud je pismeno slova v uzivateli zadaymi pismeny, pridam do docasneho slova
                # a vymazu okurenci toho pismena v docasnych pismenech
                curr_word += words[word][letter]
                letters_temp = letters_temp.replace(words[word][letter], '')
        # pokud se slovo sestavene z moznych pismen rovna danemu slovu, je validni
        if curr_word == words[word]:
            valid_words.append(curr_word)

    # print(valid_words)

    # vrati nejdels slovo z validnich slov
    return max(valid_words, key=len)

if __name__ == '__main__':
    path = input('Zadej relativni cestu k pozadovanemu souboru: ')
    # letters = input('Zadej písmena, které máš k dispozici: ')
    letters = 'aférbyb'
    if len(letters) < 1 or len(letters) > 10:
        print('pozadovany pocet tvych pismen je 1 až 10')
        quit()
    else:
        print(scrabble(path, letters))
