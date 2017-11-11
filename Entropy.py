import copy
from numpy import float
import random

"""
Entrospector
Research project for Dr. Bryan Pickett
Developed by Piotr Senkow
November 10, 2017
"""

class Entropy:

    def __init__(self,filename):
        self.filename = filename
        self.d = {}
        self.counts = {}
        self.duplicated_system = {}
        self.duplicatecounts = {}

        """
        CREATE DICTIONARY FOR ORIGINAL SYSYEM. 
        KEY = NODE, Value = list of nodes 
        """
        with open(filename) as f:
            for line in f:
                (key, val) = line.split()  # split each lines so first number is key and the second one is its connecting node
                key = int(key)
                val = int(val)
                self.d.setdefault(key, []).append(val)  # method that adds multiple vals to a key and throws the nodes and its connections to d dictionary
        """
        CREATE COUNTS FOR ORIGINAL SYSTEM
        """
        for key, val, in self.d.items():  # Loop takes each key in d (gene node) and counts amount of items to each key. Places the node in dictionary "counts" as a key
            NumOfItems = len(self.d[key])  # and then the number corresonding to how many connections in d as the value in dictionary "counts"
            self.counts[key] = NumOfItems
        """
        CREATE NEGATIVE KEYS AND COPY ALL THE LIST VALUES TO NEGATIVE KEY VALUES IN DUPLICATION NETWORK
        IMPORTANT TO COPY THE LISTS CORRECTLY SO I COPY THE ACTUAL LIST AND NOT THE REFERENCE 
        """
        for key,val in self.d.items():

            self.duplicated_system[key]=copy.copy(self.d.get(key)) #put the values into copy dictionary for the same keys
            negkey = -key #change key to a negative key
            self.duplicated_system[negkey]=copy.copy(self.d.get(key)) #add those negative keys to dictionary with lists as values
        """
        CREATE NEGATIVE NODES FOR LISTS WITHIN DUPLICATED NETWORK 
        """
        for key, val in self.duplicated_system.items(): #iterate through copy dictionary, creates a temp list, throws values of each list into temp list, turns them negative, extend original list with the temp list holding negative values (duplication)
            templist=[]
            for x in self.duplicated_system[key]: #take lists items, make them negative and append them to a temporary list
                templist.append(-x)
            self.duplicated_system[key].extend(templist) #extend the list in duplicated system with the negative values
            del templist[:] #delete temp list to avoid memory leak with the next iteration
        """
        CREATE A DICTIONARY FOR THE COUNTS OF DUPLICATED SYSTEM
        """
        for key, val, in self.duplicated_system.items():  # Loop takes each key in d (gene node) and counts amount of items to each key. Places the node in dictionary "counts" as a key
            NumOfItems = len(self.duplicated_system[key])  # and then the number corresonding to how many connections in d as the value in dictionary "counts"
            self.duplicatecounts[key] = NumOfItems


    def print_network(self):
        for x in self.d:  # iterates through whole dictionary
            print("{} : {}".format(x, self.d[x]))  # prints key and all values attached to it

        for x in self.counts:  # iterates through "counts" dictionary and displays the nodes their number of connections
            print("Gene {} connects to {} genes".format(x, self.counts[x]))

    def print_duplicate_network(self):
        for x in self.duplicated_system:  # iterates through whole dictionary
            print("{} : {}".format(x, self.duplicated_system[x]))  # prints key and all values attached to it

        for x in self.duplicatecounts:  # iterates through "counts" dictionary and displays the nodes their number of connections
            print("Gene {} connects to {} genes".format(x, self.duplicatecounts[x]))

    def calculate_network_entropy(self):
        total_entropy= 0
        for x in self.counts:
            number_of_connections = self.counts[x]
            if number_of_connections == 1:  # if there's only one connection, no entropy
                number_of_connections = 0
            total_entropy += number_of_connections
        print("1/{}".format(total_entropy))  # test to see what denominator is
        total_entropy = 1 / float(total_entropy)  # total entropy calculation
        print("The total entropy of the entire system is {}\n".format(total_entropy))

    def calculate_duplicate_entropy(self):
        total_entropy= 0
        for x in self.duplicatecounts:  # for loop that accesses count values of each value in counts dictionary and adds them to totalentropy
            number_of_connections = self.duplicatecounts[x]
            if number_of_connections == 1:  # if there's only one connection, no entropy
                number_of_connections = 0
            total_entropy += number_of_connections
        print("1/{}".format(total_entropy))  # test to see what denominator is
        total_entropy = 1 / float(total_entropy)  # total entropy calculation
        print("The total entropy of the duplicated system is {}\n".format(total_entropy))

    def duplicated_length(self): #check how many nodes left in duplicated system
        print("The duplicated graph currently has {} nodes".format(len(self.duplicated_system)))


    """
    10% graph degeneration for now 
    """
    def degeneration(self):
        print("Degenerating 10% of the graph\n")
        degeneration_constant= len(self.duplicated_system) #grab number of nodes in duplicated system
        K= int(degeneration_constant*0.10)
        j=0
        while j<K: #
            key, val = random.choice(list(self.duplicated_system.items())) #choose a random node in duplicated system

           #print("Node {} connects to {}\n".format(key, val))

            temp_list=copy.copy(self.duplicated_system.get(key)) #create a temporary list of all connections to the node for visiting

            """
            Currently loop is set up that if a connection is deleted from a node and there's no connection left, it will delete that node too
            """
            for i in range(0, len(self.duplicated_system.get(key))): #for loop that visits each node that connects to node in question, and deletes its instance in their connections.
                #print(temp_list[i])
                #print(self.duplicated_system.get(temp_list[i]))
                self.duplicated_system.get(temp_list[i]).remove(key)
                #print(self.duplicated_system.get(temp_list[i]))
                if not self.duplicated_system.get(temp_list[i]): #if there remain 0 connections after all instances were deleted, delete that node too. Cannot exist alone.
                    self.duplicated_system.pop(temp_list[i])
                    self.duplicatecounts.pop(temp_list[i])
                    j=j+1

            self.duplicated_system.pop(key,None) #once visited all the connections and deleted all instances of the node in question, DELETE THE KEY VALUE FOR THAT NODE
            self.duplicatecounts.pop(key,None) #DELETE IT FROM COUNTS TOO SO ENTROPY GETS AFFECTED
            j=j+1