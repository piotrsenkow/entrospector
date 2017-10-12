import sys                             #Modules
from numpy import float

d = {}                                 #Data structures
counts = {}

def Quit():                            #Kill program >:)
    sys.exit()

def PrintNetwork(): #prints all the genes and what they connect to
    for x in d:  # for each value in dictionary
        print("{} : {}".format(x, d[x]))  # prints key and all values attached to it
    Menu()

def PrintSet(): #print an individual key
    key = input("Which gene would you like to see all of its connections to?\n")
    key = str(key)
    print(d.get(key))
    Menu()

def DlenPrint(): #print length of the dictionary
    print(len(d))
    Menu()

def PrintSystemsCounts():
    for x in counts:  # for loop that prints out the gene and how many genes it connects to, iterating through the "counts" dictionary
        print("Gene {} connects to {} genes".format(x, counts[x]))
    Menu()

def PrintSetsCounts():
    key=input("Which gene would you like to see the number of connections to?\n")
    key = str(key)
    print(counts.get(key))
    Menu()

def PrintGeneInformation():
    key = input("Which gene would you like more information about?\n")
    key = str(key)
    print("{} has {} genes connect to it".format(key, counts.get(key)))
    print("{} has the following genes connect to it: {}".format(key, d.get(key)))
    Menu()

def PrintIndividualEntropy():
    key=input("Which gene's entropy would you like to know?\n")
    key = str(key)
    entropy = counts.get(key)  # code segment for calculating entropy value of that gene
    entropy = 1 / float(entropy)  # float type necessary unless you want python to tell you 0 entropy calculated
    print("The entropy of gene {} is {} because {} genes connect to it".format(key, entropy, counts.get(key)))
    Menu()

def PrintSystemEntropy():
    totalentropy = 0  # total entropy counter set to 0
    for x in counts:  # for loop that accesses count values of each value in counts dictionary and adds them to totalentropy
        entropy = counts[x]
        totalentropy += entropy
    print("1/{}".format(totalentropy))  # test to see what denominator is
    totalentropy = 1 / float(totalentropy)  # total entropy calculation
    print("The total entropy of the entire system is {}".format(totalentropy))
    Menu()

def Menu():            #Main Menu
    menu = {1: PrintNetwork, 2: PrintSet, 3: DlenPrint, 4: PrintSystemsCounts, 5: PrintSetsCounts,
            6: PrintGeneInformation, 7: PrintIndividualEntropy, 8: PrintSystemEntropy, 0: Quit}
    num = input()
    menu[num]()

def main():
    with open("Yeast.txt") as f:  # while the text is open
        for line in f:  # iterate through each line
            (key, val) = line.split()  # split each lines so that its key then value
            d.setdefault(key, []).append(val)  # method that adds multiple vals to a key
    for key, val, in d.items():  # prints the key and the number of values there
        NumOfItems = len(filter(bool, val))
        counts[key] = NumOfItems
    Menu()


if __name__ == "__main__":
    # execute only if run as a script
    main()