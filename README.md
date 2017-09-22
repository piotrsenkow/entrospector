# entrospector

Two Bugs: 

1). It only runs in Python 2.7.12 so to run it run the command in your terminal "python Entropy.py". If you try running it in python 3 you will get a "TypeError: object of type 'filter' has no len()"

2). Line 26 of code, when you want to find out the amount of genes that connect to a specific node, you cant type in a specific number like 1369 or else you will get "1369 has None genes connect to it." It will only work if you type in the node like '1369' 