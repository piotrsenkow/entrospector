# Entrospector

# A research project in the works written in Python by Piotr Senkow for Dr. Bryan Pickett,  Loyola University Chicago.

Entrospector takes an input file of genes and maps out all of the connections in a connected graph system. 
The program currently has several capabilities: Print out all nodes in the system and each node's connections/search for a specific node and print its connections or number of connections, calculate how many unique nodes in the system, calculate the entropy value of individual nodes or of the entire system, and graph duplication.
Entrospector can also degenerate the duplicate genome, deleting 10 percent of the system's nodes and connections at random. Since the entropy value of the system can change everytime as degeneration is random, entrospector can recreate duplication, degeneration, and calculation of total entropy over 10 times - calculating the average entropy value. 

Entropy is the uncertainty of which connections a node will connect to in a system.
Also, the Entropy score is the total edge information of the network, which we designate as the Static Network Total Information (Hstat). It is calculated using the equation(H= ∑log(2)F) , simply representing the sum of all individual nodes and edges in the network.
For example, gene "A" connects to only gene "B". There is zero uncertainty that gene "A" will connect to anything other than "B". However, if gene "A" connected to gene "C" and gene "D" then the certainty the certainty that gene "A" will connect to gene "C" is only 50% since it has the option of connecting to either "C" or "D".
Therefore, the Entropy score of an entire system is simply the sum of all Entropy scores of each node in the system. 

Since genetic networks oftentimes duplicate, Entrospector has the ability to simulate the duplication of the graph. Duplicated nodes are simply denoted as negative values (gene "1" duplicates to gene "-1") and the duplicated system connects to the original system (aside from nodes and their duplicates). For example if in the original system gene "1" connected to gene "2", that would mean gene "2" connects to gene "1". When the system duplicates there are then 4 nodes in play, "1", "2", "-1", "-2". Gene "1" then connects to gene "2" and "-2", however, gene "1" doesn't connect to gene "-1".

More biological phenomena that are simulated in this program will be explained upon release of the scientific paper.

# Features coming soon:
A GUI, Py2Cytoscape for user-friendly visualization of genetic graph in real-time, statistical analysis.
