# entrospector

# A research project in the works written for Dr. Brian Pickett, Loyola University Chicago.

Entrospector takes an input file of genes and their connections and creates a dictionary
that houses them.
Entrospector has the capability to check how many unique connections each gene has, allowing the user to specify a gene of interest and see how the network intereacts.
Entrospector also calculates an entropy score for individual genetic nodes and of the system as a whole.
GUI and a way to visualize the network as a connected graph coming soon! 

#Problems to fix:
Duplication works, but then original dataset gets overwritten and you can't see pre-duplication system.
If you run option 9 multiple times it duplicates but the nodes that connections are wrong. Need to implement a way for user to not be able to duplicate a second time.