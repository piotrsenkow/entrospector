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

    def __init__(self, system, system_counts, duplicate, duplicate_counts):
        self.genome = system
        self.genome_counts = system_counts
        self.duplicated_system = copy.deepcopy(duplicate)
        self.duplicate_counts = copy.deepcopy(duplicate_counts)

    def send_dictionary(self):
        return self.genome

    def print_network(self):
        for x in self.genome:  # prints each node and its connections in genome
            print("{} : {}".format(x, self.genome[x]))

        for x in self.genome_counts:  # prints the number of connections for each node in genome
            print("Gene {} connects to {} genes".format(x, self.genome_counts[x]))

    def print_duplicate_network(self):
        for x in self.duplicated_system:  # prints each node and its connections in duplicate genome
            print("{} : {}".format(x, self.duplicated_system[x]))

        for x in self.duplicate_counts:  # prints the number of connections for each node in duplicate genome
            print("Gene {} connects to {} genes".format(x, self.duplicate_counts[x]))

    def calculate_network_entropy(self):
        total_entropy = 0
        for x in self.genome_counts:
            number_of_connections = self.genome_counts[x]
            if number_of_connections == 1:  # if there's only one connection, no entropy
                number_of_connections = 0
            total_entropy += number_of_connections  # adds to the growing denominator
        print("1/{}".format(total_entropy))  # test to see what denominator is
        total_entropy = 1 / float(total_entropy)  # total entropy calculation
        print("The total entropy of the entire system is {}\n".format(total_entropy))

    def calculate_duplicate_entropy(self):
        total_entropy= 0
        for x in self.duplicate_counts:  # calculates entropy of duplicate entropy accessing duplicate counts dictionary
            number_of_connections = self.duplicate_counts[x]
            if number_of_connections == 1:  # if there's only one connection, no entropy
                number_of_connections = 0
            total_entropy += number_of_connections
        print("1/{}".format(total_entropy))  # test to see what denominator is
        total_entropy = 1 / float(total_entropy)  # total entropy of duplicate genome calculation
        print("The total entropy of the duplicated system is {}\n".format(total_entropy))
        return total_entropy

    def duplicated_length(self):  # check how many nodes left in duplicated system
        print("The duplicated graph currently has {} nodes".format(len(self.duplicated_system)))

    def degeneration(self):
        print("Degenerating 10% of the graph\n")
        degeneration_constant= len(self.duplicated_system)  # grab number of nodes in duplicated system
        constant = int(degeneration_constant*0.10)  # constant is calculated to know how many nodes to delete
        j = 0  # iterator so degeneration ends after a "constant" amount of nodes are deleted

        while j < constant:  # loop that deletes a node and all instances of node in its connections
            key, val = random.choice(list(self.duplicated_system.items()))  # choose a random node to delete
            temp_list = copy.copy(self.duplicated_system.get(key)) # temp list of all connections of node to be deleted

            """
            Currently loop is set up that if a connection is deleted from a node and there's no connection left, 
            it will delete that node too
            """

            for i in range(0, len(self.duplicated_system.get(key))):
                # for loop that visits each node that connects to node in question,
                # and deletes its instance in their connections.

                # unit tests to be implemented
                # print(temp_list[i])
                # print(self.duplicated_system.get(temp_list[i]))

                self.duplicated_system.get(temp_list[i]).remove(key)
                # print(self.duplicated_system.get(temp_list[i]))

                if not self.duplicated_system.get(temp_list[i]):
                    # if there remain 0 connections after all instances were deleted, delete that node too.
                    # Cannot exist alone.
                    self.duplicated_system.pop(temp_list[i])
                    self.duplicate_counts.pop(temp_list[i])
                    j = j+1

            self.duplicated_system.pop(key,None)
            # once visited all the connections and deleted all instances
            # of the node in question, DELETE THE KEY VALUE FOR THAT NODE
            self.duplicate_counts.pop(key, None)
            # DELETE IT FROM COUNTS TOO SO ENTROPY GETS AFFECTED
            j += 1
