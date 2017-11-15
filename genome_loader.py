import copy

"""
Entrospector
Research project for Dr. Bryan Pickett
Developed by Piotr Senkow
November 10, 2017
"""


class Loader:

    def __init__(self,filename):
        self.filename = filename
        self.genome = {}
        self.genome_counts = {}
        self.duplicated_genome = {}
        self.duplicate_counts = {}

        with open(filename) as f:
            for line in f:
                (key, val) = line.split()  # split lines so first number is key & the second one is its connecting node
                key = int(key)
                val = int(val)
                self.genome.setdefault(key, []).append(val)
                # method that adds multiple values to a key and throws the nodes and its connections to genome dict.
        """
        CREATE COUNTS FOR EACH NODE IN GENOME
        """
        for key, val, in self.genome.items():
            # counts number of connections of each node in genome
            # places node and number of connections in genome_counts dictionary
            number_of_connections = len(self.genome[key])
            self.genome_counts[key] = number_of_connections
        """
        CREATE NEGATIVE KEYS AND COPY ALL THE LIST VALUES TO NEGATIVE KEY VALUES IN DUPLICATION NETWORK
        IMPORTANT TO COPY THE LISTS CORRECTLY SO I COPY THE ACTUAL LIST AND NOT THE REFERENCE 
        """
        for key, val in self.genome.items():
            self.duplicated_genome[key] = copy.copy(self.genome.get(key))  # copy nodes into duplicate dict.
            negative_key = -key  # change key to a negative key
            self.duplicated_genome[negative_key] = copy.copy(self.genome.get(key))
            # add negative nodes and copy the lists of connections from corresponding positive nodes
        """
        CREATE NEGATIVE CONNECTIONS IN DUPLICATE GENOME DICTIONARY
        """
        for key, val in self.duplicated_genome.items():
            # iterate through copy dictionary, creates a temp list, throws values of each list into temp list,
            # turns them negative, extend original list with the temp list holding negative values (duplication)
            temp_list = []
            for x in self.duplicated_genome[key]:
                # take lists items, make them negative and append them to a temporary list
                temp_list.append(-x)
            self.duplicated_genome[key].extend(temp_list)
            # extend the list in duplicated system with the negative values
            del temp_list[:]  # delete temp list to avoid memory leak with the next iteration
        """
        CREATE A DICTIONARY FOR THE COUNTS OF DUPLICATED SYSTEM
        """
        for key, val, in self.duplicated_genome.items():
            number_of_connections = len(self.duplicated_genome[key])
            self.duplicate_counts[key] = number_of_connections

    def get_system(self):
        return self.genome

    def get_counts(self):
        return self.genome_counts

    def get_duplicate_system(self):
        return self.duplicated_genome

    def get_duplicate_count(self):
        return self.duplicate_counts
