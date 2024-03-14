#fonctions
###############################################################################
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

def score(word:str):
    points={'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,'j':8,'k':10,
            'l':1,'m':2,'n':1,'o':1,'p':3,'q':8,'r':1,'s':1,'t':1,'u':1,'v':4,
            'w':10,'x':10,'y':10,'z':10}
    letter=list(word)
    pts=0
    for i in range(len(letter)):
        pts+=points[letter[i]]
    return(pts)

def max_score(words:list):
    number,pts=0,score(words[0])
    for i in range(1,len(words)):
        if score(words[i])>pts:
            number,pts=i,score(words[i])
    return(words[number],pts)


def best_word(words:list,letters:list):
    """
    Parameters
    ----------
    words : list of string
        words available
    letters : list of string
        letters available
        
    Returns the words that give the maximum of points.
    -------
    """
    available_words=[]
    for i in range(len(words)):
        copy_letters=letters.copy()
        if possible_word(words[i], copy_letters):
            available_words.append(words[i])
    return(max_score(available_words))
###############################################################################

words=word_initialization("mots.sansaccent.txt")
letters=['o','s','a','u','s','n','g','w']
print(best_word(words,letters))




