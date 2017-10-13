import sys                             #Modules
from numpy import float
import time

d = {}                                 #Data structures
counts = {}

def Quit():    #Kill program >:)
    sys.exit()

def PrintNetwork(): #prints all the genes and what they connect to
    start_time = time.time()
    for x in d:  # for each value in dictionary
        print("{} : {}".format(x, d[x]))  # prints key and all values attached to it
    elapsed_time = time.time() - start_time
    print("{} seconds to complete task".format(elapsed_time))
    input("press enter to return to menu")
    Menu()

def PrintSet(): #print an individual key
    key = input("Which gene would you like to see all of its connections to?\n")
    start_time = time.time()
    key = str(key)
    print(d.get(key))
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
    for x in counts:  # for loop that prints out the gene and how many genes it connects to, iterating through the "counts" dictionary
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

def PrintSystemEntropy():
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
    input("press any key to return to menu")
    Menu()

def Menu():            #Main Menu with dictionary containing options( mimicing a switch case statement)
    menu = {1: PrintNetwork, 2: PrintSet, 3: DlenPrint, 4: PrintSystemsCounts, 5: PrintSetsCounts,
            6: PrintGeneInformation, 7: PrintIndividualEntropy, 8: PrintSystemEntropy, 0: Quit}
    f=open("options.txt") #don't want to put menu options into memory so reading from a file
    for line in f: #prints menu
        print(line)
    f.close() #closes file reader to conserve memory
    num = input()
    num=int(num)
    if 0<=num<=8: #if user input is one of the options execute the method
        menu[num]()
    else:
        input("Please choose an option between 0 and 8\nPress enter to continue")
        Menu()


def main():
    with open("Yeast.txt") as f:  # while the text is open
        for line in f:  # iterate through each line
            (key, val) = line.split()  # split each lines so that its key then value
            d.setdefault(key, []).append(val)  # method that adds multiple vals to a key and throws the nodes and its connections to d dictionary
    for key, val, in d.items():  # for loop that puts each node and the amount of values it connects to into a dictionary called counts
        NumOfItems = len(d[key])
        counts[key] = NumOfItems
    Menu() #method for main menu


if __name__ == "__main__":
    # execute only if run as a script
    main()