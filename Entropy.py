from numpy import float
#http://code.activestate.com/recipes/52219-associating-multiple-values-with-each-key-in-a-dic/
d = {}                                     #creates an empty dictionary
counts = {}                                #empty dictionary thaat will hold the value counts of dictionary d
with open ("Yeast.txt") as f:              #while the text is open
    for line in f:                         #iterate through each line
        (key,val) = line.split()           #split each lines so that its key then value
        d.setdefault(key,[]).append(val)   #method that adds multiple vals to a key

for x in d:                                #for each value in dictionary
    print("{} : {}".format(x,d[x]))        #prints key and all values attached to it

print("test\n")
print(d.get('1369'))                       #prints values ['815', '859', '941'] for key 1369

for key, val, in d.items():                #prints the key and the number of values there
    print(key, len(filter(bool,val)))      #len(filter(bool,val))) necessary methods for counting the values present in the dictionary
    NumOfItems= len(filter(bool,val))
    counts[key]= NumOfItems                #places the number of items contained to a value into the "counts" dictionary.
print(len(d))                              #prints the length of dictionary

for x in counts:                           #for loop that prints out the gene and how many genes it connects to, iterating through the "counts" dictionary
    print("Gene {} connects to {} genes".format(x,counts[x]))
print(counts.get('1369'))                  #test to see if I can access gene number 1369 and see how many other genes it connects to

                                           #here the user inputs what gene it wants to access:
answer = input('Which gene would you like to know about?\n')
answer=str(answer)                         #convert the answer to a string to fix problem of accessing dictionary with an int value without single quotes (' ')
print("{} has {} genes connect to it".format(answer,counts.get(answer)))
print("{} has the following genes connect to it: {}".format(answer,d.get(answer)))
                                           #prints information of gene - what genes connects to it and how many of them

entropy = counts.get(answer)               #code segment for calculating entropy value of that gene
print(entropy)
entropy= 1/float(entropy)                  #float type necessary unless you want python to tell you 0 entropy calculated
print("The entropy of gene {} is {} because {} genes connect to it".format(answer,entropy, counts.get(answer)))

totalentropy = 0                           #total entropy counter set to 0
for x in counts:                           #for loop that accesses count values of each value in counts dictionary and adds them to totalentropy
    entropy=counts[x]
    totalentropy+=entropy
print(totalentropy)                        #test to see what denominator is
totalentropy=1/float(totalentropy)         #total entropy calculation
print("The total entropy of the entire system is {}".format(totalentropy))