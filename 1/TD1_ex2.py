def word_initialization(words:list,text:str):
    """
    fonction that return a list of words with 8 or less letters 
    from a external sources
    """
    file = open(text,'r')
    for line in file:
        if len(line[0:len(line)-1])<=8:
            words.append(line[0:len(line)-1])

    file.close()
    return(words)



        