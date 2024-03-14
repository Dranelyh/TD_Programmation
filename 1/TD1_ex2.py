def word_initialization(text:str):
    """
    fonction that return a list of words with 8 or less letters 
    from a external sources.
    """
    words=[]
    file = open(text,'r')
    for line in file:
        if len(line[0:len(line)-1])<=8:
            words.append(line[0:len(line)-1])

    file.close()
    return(words)

def possible_word(word:str,letters:list):
    """
    Returns True if the word could be writen with the elements of letters.
    -------
    """
    word_letter=list(word)
    for i in range(len(word_letter)):
        if word_letter[i] not in letters:
            return(False)
        else:
            letters.pop(letters.index(word_letter[i]))
    return(True)

def longest_word(words:list,letters:list):
    """
    Parameters
    ----------
    words : list of string
        words available
    letters : list of string
        letters available
        
    Returns the longest words with the available letters.
    -------
    """
    longest=''
    for i in range(len(words)):
        copy_letters=letters.copy()
        if len(longest)==8:
            return(longest)
        elif possible_word(words[i], copy_letters) and len(longest)<len(words[i]):
            longest=words[i]
    return(longest)
            
    
    
    
    
###############################################################################
words=word_initialization("mots.sansaccent.txt")
letters=['o','s','o','u','s','i','n','r']
longest=longest_word(words, letters)
print(longest)

