import sys                             #Modules
from numpy import float
import time

d = {}                                 #Data structures
counts = {}

def Quit():    #Kill program >:)
    sys.exit()

def PrintNetwork(): #prints all the genes and their connections
    start_time = time.time()
    for x in d:  # iterates through whole dictionary
        print("{} : {}".format(x, d[x]))  # prints key and all values attached to it
    elapsed_time = time.time() - start_time
    print("{} seconds to complete task".format(elapsed_time))
    input("press enter to return to menu")
    Menu()

def PrintSet(): #print an individual key and its connections
    key = input("Which gene would you like to see all of its connections to?\n")
    start_time = time.time()
    key = str(key)
    print(d.get(key)) #prints the value of the key that user specifies
    elapsed_time = time.time() - start_time
    print("{} seconds to complete task".format(elapsed_time))
    input("press enter to return to menu")
    Menu()

def DlenPrint(): #print length of the dictionary
    start_time = time.time()
    print("There are {} nodes".format(len(d)))
    elapsed_time = time.time() - start_time
    print("{} seconds to complete task".format(elapsed_time))
    input("press enter to return to menu")
    Menu()

def PrintSystemsCounts(): #prints each node in system and how many connections each node has
    start_time = time.time()
    for x in counts:  # iterates through "counts" dictionary and displays the nodes their number of connections
        print("Gene {} connects to {} genes".format(x, counts[x]))
    elapsed_time = time.time() - start_time
    print("{} seconds to complete task".format(elapsed_time))
    input("press enter to return to menu")
    Menu()

def PrintSetsCounts(): #method allows you to specify a node in question and see how many connections it has
    key=input("Which gene would you like to see the number of connections to?\n")
    start_time = time.time()
    key = str(key)
    print(counts.get(key))
    elapsed_time = time.time() - start_time
    print("{} seconds to complete task".format(elapsed_time))
    input("press enter to return to menu")
    Menu()

def PrintGeneInformation(): #method prints what genes connect to a specific node and how many of them
    key = input("Which gene would you like more information about?\n")
    start_time = time.time()
    key = str(key)
    print("{} has {} genes connect to it".format(key, counts.get(key)))
    print("{} has the following genes connect to it: {}".format(key, d.get(key)))
    elapsed_time = time.time() - start_time
    print("{} seconds to complete task".format(elapsed_time))
    input("press enter to return to menu")
    Menu()

def PrintIndividualEntropy():
    key=input("Which gene's entropy would you like to know?\n")
    start_time = time.time()
    key = str(key)
    entropy = counts.get(key)  # calculates entropy value of that gene
    entropy = 1 / float(entropy)  # float type necessary unless you want python to tell you 0 entropy calculated
    print("The entropy of gene {} is {} because {} genes connect to it".format(key, entropy, counts.get(key)))
    elapsed_time = time.time() - start_time
    print("{} seconds to complete task".format(elapsed_time))
    input("press enter to return to menu")
    Menu()

def PrintSystemEntropy(): #prints out the systems total entropy
    totalentropy = 0  # total entropy counter set to 0
    start_time = time.time()
    for x in counts:  # for loop that accesses count values of each value in counts dictionary and adds them to totalentropy
        entropy = counts[x]
        totalentropy += entropy
    print("1/{}".format(totalentropy))  # test to see what denominator is
    totalentropy = 1 / float(totalentropy)  # total entropy calculation
    print("The total entropy of the entire system is {}".format(totalentropy))
    elapsed_time = time.time() - start_time
    print("{} seconds to complete task".format(elapsed_time))
    input("press enter to return to menu")
    Menu()

def Menu(): #Main Menu with dictionary containing options( mimicing a switch case statement)
    menu = {1: PrintNetwork, 2: PrintSet, 3: DlenPrint, 4: PrintSystemsCounts, 5: PrintSetsCounts,         #Dictionary of menu options
            6: PrintGeneInformation, 7: PrintIndividualEntropy, 8: PrintSystemEntropy, 0: Quit}

    f=open("options.txt") #don't want to put menu options into memory so reading from a file
    for line in f: #prints menu
        print(line)
    f.close() #closes file reader to conserve memory
    num = input() #gets users menu option choice

    try:
        num = int(num) #try to see if the user put in an integer value
    except ValueError: #if it isn't tell the user to put a number in and return to menu
        print("That's not a number! Returning to menu")
        input("press enter to return to menu")
        Menu()

    else: #otherwise proceed with the menu
        if 0<=num<=8: #if user input is one of the options execute one of the programs methods
            menu[num]()
        else: #if the user chooses a number that isn't an option in the menu
            print("Choose one of the menu options. Returning to menu.")
            input("press enter to return to menu")
            Menu()

def main():
    with open("Yeast.txt") as f:  # while the text is open
        for line in f:  # iterate through each line
            (key, val) = line.split()  # split each lines so that its key then value
            d.setdefault(key, []).append(val)  # method that adds multiple vals to a key and throws the nodes and its connections to d dictionary
    for key, val, in d.items():   #Loop takes each key in d (gene node) and counts amount of items to each key. Places the node in dictionary "counts" as a key
        NumOfItems = len(d[key])  #and then the number corresonding to how many connections in d as the value in dictionary "counts"
        counts[key] = NumOfItems
    Menu() #method for main menu


if __name__ == "__main__":
    # execute only if run as a script
    main()