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
    print(key, len(filter(bool,val)))
    NumOfItems= len(filter(bool,val))
    counts[key]= NumOfItems
print(len(d))                              #prints the length of dictionary

for x in counts:
    print("Gene {} connects to {} genes".format(x,counts[x]))





