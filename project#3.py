
def searchC(word):
    pass

def searchP(word):
    pass

def searchR(word):
    pass

def encode():
    pass

def email():
    pass


inp = input("Input a file name. ex. \"filename\".txt \n")
with open(imp+".txt", "r") as myFile:
    text_main = myFile.read()
    myFile.seek(0)






#starts program, greets the user, displays the starting menu
#Ask for the text file name
#1 Search/count word or phrase
#2 Search and print a section of text (100 characters) (cycle through occurances)
#3 search and replace, let the user know that its completed
#4 Encode using caesar shift code and save as a file
#5 Email a random section of text to a user input email address
#6 One other feature of my choice
#6v2 start running the guessing game lol
#7 Quit with a farewell
