from Entropy import Entropy
from genome_loader import Loader
import time

"""
Entrospector
Research project for Dr. Bryan Pickett
Developed by Piotr Senkow
November 10, 2017
"""

if __name__ == "__main__":
    entropy_list = []  # Holds entropy values of degenerated duplicated systems

    start_time = time.time()
    y = Loader('Yeast.txt')
    genome_system = y.get_system()
    genome_counts = y.get_counts()
    duplicate_genome = y.get_duplicate_system()
    duplicate_counts = y.get_duplicate_count()

    degeneration_iterator = 0
    while degeneration_iterator < 10:
        x = Entropy(genome_system, genome_counts, duplicate_genome, duplicate_counts)
        # x.print_network()
        # x.print_duplicate_network()
        # x.calculate_network_entropy()
        x.calculate_duplicate_entropy()
        # x.duplicated_length() #how many nodes in duplicated system
        x.degeneration()
        # x.print_duplicate_network()
        entropy = x.calculate_duplicate_entropy()
        entropy_list.append(entropy)
        # x.duplicated_length()
        del x  # free object from memory
        degeneration_iterator += 1

    total = 0.0
    i = 0  # iterator counter to add all entropy values that are products of degeneration to calc average
    while i < len(entropy_list):
        total += entropy_list[i]
        i += 1
    print("{} \n".format(entropy_list))  # calculates average entropy value
    print("Average entropy over 10 trials of duplication and random degeneration at 10% is {} ".format(total / (len(entropy_list))))
    elapsed_time = time.time() - start_time
    print("{} seconds to complete task".format(elapsed_time))