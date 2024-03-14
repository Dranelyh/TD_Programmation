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
    Returns True if the word could be writen with the elements of letters, 
    the associated word without the letter from a joker and a tupple formed
    with the letter replaced by a joker and it position in the word.
    -------
    """
    assert letters.count('?')<=1, "Too many joker"
    
    word_letter=list(word)
    joker=None
    for i in range(len(word_letter)):
        if (word_letter[i] not in letters) and ('?' not in letters):
            return(False,'',None)
        elif word_letter[i] in letters:
            letters.pop(letters.index(word_letter[i]))
        else:
            letters.pop(letters.index('?'))
            joker=i #index of the letter replaced with a joker
    if joker==None:
        return(True,word,None)
    else:
        missing_letter=word_letter[joker]
        word_letter.pop(joker)
        joker_word=''
        for i in range(len(word_letter)):
            joker_word+=word_letter[i]
        return(True,joker_word,(missing_letter,joker))

def score(word:str):
    points={'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,'j':8,'k':10,
            'l':1,'m':2,'n':1,'o':1,'p':3,'q':8,'r':1,'s':1,'t':1,'u':1,'v':4,
            'w':10,'x':10,'y':10,'z':10,'?':0} #add ? value
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
    return(words[number],pts,number) #now return the index to simplify best_word


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
    joker=[]
    for i in range(len(words)):
        copy_letters=letters.copy()
        data=possible_word(words[i], copy_letters)
        if data[0]:
            available_words.append(data[1])
            joker.append(data[2])
    scr=max_score(available_words)
    complete_word=scr[0][:(joker[scr[2]][1])]+joker[scr[2]][0]+scr[0][(joker[scr[2]][1]):]
    return(complete_word,scr[1])
###############################################################################

words=word_initialization("mots.sansaccent.txt")
letters=['z','x','c','v','r','r','t','?']
print(best_word(words,letters))