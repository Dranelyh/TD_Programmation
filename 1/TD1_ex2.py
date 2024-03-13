words=[]

file = open("frenchssaccent.dic",'r')
for line in file:
    words.append(line[0:len(line)-1])

file.close()

