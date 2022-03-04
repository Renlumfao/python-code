Sentence = input("Enter your Sentence: ")#The user has to input their Sentence.
print("Your Sentence was:",Sentence)#This will display the user input.
Sentence = Sentence.upper().split()#This will make the user statement into uppercase and into an array.

Word_List = []#The unique vaules of the user Sentence.
Index_List = [] #This will contain all the indices that will be asigned to a word for the user Sentence.
Sequence_List = [] #This will contain the indices but in order of the user Sentence.

#[] means it's an empty array.
##For the FOR LOOP##
#Indices is where the numbers will be entered.
#Item is in which each item of the Sentence.
#The for loop is giving each item(word in the variable 'Sentence') it's own index number, therefore we can start creating our Sequence.

for indices, item in enumerate(Sentence):#Go though each word in the array and gives them a number.
    if item not in Word_List: #if the item (A word in the variable 'Sentence') is not in the varaible 'Word_List' then it's not unique.
        Word_List.append(item)#This will grab the unique words and append it to the variable 'Word_list'
        #This will also make it so that it remove any duplicate as it won't enter the same word in again.
        Index_List.append(indices+1)#This will grab a unique number and add it to the variable 'Index_list' so a unique Word is assigned with a number.
        #This will also remove the number for any duplicate words that appered in the user Sentence.
    Sequence_List.append(Sentence.index(item)+1)#.index finds where the original word was found.

print("These are the unique words found in your sentence,",Word_List)#This will print out the unique words in the user sentence.
print("\nThese are the numbers that are asigned to the unique words,",Index_List)#This will print out the numbers asigned to the unique words.
print("\nThis is what your sentence looks like in a sequence,",Sequence_List)#This will print out the sequence made out of the numbers.

File = open("Word_List.txt", "w")#This will create a text file that named Word_List and holds what is contained in the variable Word_List.
File.write(str(Word_List))
File.close()

File3 = open("Index_List.txt", "w")#This will create a text file named Index_List and holds what is contained in the variable Index_List.
File3.write(str(Index_List))
File3.close()

File2 = open("Sequence_List.txt", "w")#This will create a text file named Sequence_List and holds what is contained in the variable Sequence_List.
File2.write(str(Sequence_List))
File2.close()

print("The Word_list and Index_List as well as Sequence_List has now been saved in separate files")#This will notify the user that there work has been saved.

    

