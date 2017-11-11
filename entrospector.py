from Entropy import Entropy
import time
"""
Entrospector
Research project for Dr. Bryan Pickett
Developed by Piotr Senkow
November 10, 2017
"""

if __name__ == "__main__":
    iterator=0
    start_time = time.time()
    while iterator<10:
        x = Entropy('Yeast.txt')
        #x.print_network()
        #x.print_duplicate_network()
        #x.calculate_network_entropy()
        #x.calculate_duplicate_entropy()
        #x.duplicated_length() #how many nodes in duplicated system
        x.degeneration()
        #x.print_duplicate_network()
        x.calculate_duplicate_entropy()
        #x.duplicated_length()
        del x
        iterator+=1
    elapsed_time = time.time() - start_time
    print("{} seconds to complete task".format(elapsed_time))