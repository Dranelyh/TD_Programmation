def word_initialization(words:list,text:str):
    """
    fonction that return a list of words with 8 or less letters 
    from a external sources.
    """
    file = open(text,'r')
    for line in file:
        if len(line[0:len(line)-1])<=8:
            words.append(line[0:len(line)-1])

    file.close()
    return(words)

def possible_word(word:str,letters:list):
    """
    Returns
    True if the word could be write with the element of letters.
    -------
    """
    word_letter=list(word)
    for i in range(len(word_letter)):
        if word_letter[i] not in letters:
            return(False)
        else:
            letters.pop(letters.index(word_letter[i]))
    return(True)


