#This funcion will read the whole sentence and it will return (what it has read) the whole sentence.
def Grabword (Sentence,Separators):
    if Sentence[0] in Separators:
        Keyword = Sentence[0] 
        Sentence = Sentence[1:]
        return(Keyword,Sentence) 
    Keyword = ""
    for Character in Sentence:
        if Character.isalpha():
            Keyword = Keyword+Character
        else:
            Sentence = Sentence[len(Keyword):]#This will get rid of the first 'word' after it collects the word and displayed it
            return(Keyword, Sentence)#This will check if the next character is a part of the alphabet if not it will display word.
                            #Adding this veriable above makes it so that it will print out the Keyword and the Sentence after it.
        if Keyword == Sentence:
            Sentence = ""

    return (Keyword, Sentence)

####################Main Program####################
    
Sent = "ASK NOT WHAT YOUR COUNTRY CAN DO FOR YOU ASK WHAT YOU CAN DO FOR YOUR COUNTRY"
Separators = " " 
SearchWord = input("What would you like to search: ").upper()
WordPosition = 0
Found = False
while Sent != "":
    #pause = input()
    Word,Sent= Grabword(Sent,Separators)
    if Word not in Separators:
        WordPosition = WordPosition+1
    #print("Word =",Word)
    #print("Sentence =",Sent)
    if Word == SearchWord: #This ask you to search for what word you'll like to find
        Found = True
        print("The word",SearchWord,"was found in the position",WordPosition)
if Found == False:                  #If searchword is not in the sentence it will display 'not found'
    print(SearchWord,"was not found in the sentence.")


#Word,Sent = Grabword(Sent) 
#print(Word) 
#print(Sent)#This will get rid of the brackets
