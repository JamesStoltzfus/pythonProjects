
text_main = ""
backup = ""
x = ""

def searchCount(word,text_main):
    counted = text_main.count(word)
    print("The text '%s' shows up in the file %d times" % (word, counted))

def searchPrint(word,text_main):
    index = int(text_main.find(word))
    print(index)
##    try:
    print(text_main[index-50:index+50])
##    except:
##        print(text_main[index, index+50])
def searchReplace(word, replace, text_main):
    pass

def encode(text_main, shift):
    count = 0
def caesar(text, shift):
    lest = list(text.lower())
    values = []
    for i in range(len(lest)):
        if (ord(lest[i]) >= 97 and ord(lest[i]) <= 122):  
            values.append(chr(ord(lest[i]) + shift))
            values[i] = let_round(values[i],shift)
        else:
            values.append(lest[i])
    for i in values:
        print(i, end = "")


def let_round(letter, shift):
    if (ord(letter) >= 97 and ord(letter) <= 122):
        return letter
    if (ord(letter) < 97):
        return chr(122 - (97 - ord(letter)))
    if (ord(letter) > 122):
        return chr(96 + (ord(letter) - 122))


def checker(text):
    global count
    caesar(text[0:100],count)
    count+=1
def decode():
    global count
    for i in range(0,25):
        checker(text)
        again = input("\nshould this run again? y/n")
        if again.lower() == "n":
            caesar(text,count-1)
            count = 0
            break

def backups(text_main):
    pass

def email(user_email):
    pass

def inputF():
    global text_main, backup
    run = True
    while run:
        inp = input("Input a file name. ex. \"filename\".txt \n")
        try:
            with open(inp+".txt", "r") as myFile:
                text_main = myFile.read()
                backup = text_main
                myFile.seek(0)
                run = False
        except FileNotFoundError:
            print("That file doesn't exist, try again?")

print("Welcome to the program")
inputF()
##print(text_main)
while x != 8:
    try:
        x = int(input("Input a number 1-7 to access functions of this program\n"))
        if x == 1:
            sc = input("You've selected search count, please input a word to search for\n")
            searchCount(sc, text_main)
        elif x == 2:
            sp = input("You've seleted search print, please input a word to search\n")
            searchPrint(sp, text_main)
        elif x == 3:
            sr = input("You've entered search replace, please input a word to search for\n")
            srp = input("Now input a word to replace it with\n")
            searchReplace(sr, srp, text_main)
        elif x == 4:
            ca = input("encode function activated, input a number to shift the text by. If the input is not a number the shift will be random.\n")
            encode(text_main, ca)
        elif x == 5:
            try:
                ba = input("Backup seleted, please input the name of the file to save. 'only input this'.txt\n")
                with open(ba + ".txt", "w") as backupfile:
                    backupfile.write(text_main)
            except:
                print("file not created, please input a proper name and try again.\n")
                continue
            print("A backup of the current state of the document has been created.\n")
        elif x == 6:
            em = input("You've selected email, please input your email and a random chunk of text will be sent to you\n")
            try:
                email(em)
            except:
                print("try again with a proper email\n")
        elif x == 7:
            print("Guessing game time!\n")
        elif x == 8:
            print("Exiting program now, have a good day.\n")
    except ValueError:
        print("inproper input")
#starts program, greets the user, displays the starting menu
#Ask for the text file name
#1 Search/count word or phrase
#2 Search and print a section of text (100 characters) (cycle through occurances)
#3 search and replace, let the user know that its completed
#4 Encode using caesar shift code and save as a file
#5 Email a random section of text to a user input email address
#6 One other feature of my choice
    #saving backups
#6v2 start running the guessing game lol
#7 Quit with a farewell

