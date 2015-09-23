# -*- coding: utf-8 -*-
'''Action Neededd : 1) Please change the filepath as needed (Search for "open" and change the path 2) Please note that this program has been written on a Windows machine'''

'''Assumptions: 1) The symbols in the fileA and the lines in fileB are not corrupt i.e. no missing values, no incorrectly formatted values.
2) The symbols to be found in fileB are to be found after '=' in the line.
'''



import collections

#opening fileA - list of symbols. Please change the filepath as needed
with open('fileA.txt') as f:
    symbols = f.readlines()

#initializing a list for output	
output = []

#Opening fileB - gateway risk configuration. Please change the filepath as needed
with open('fileB.txt') as f:
    #parsing through each line
    for line in f:
        #parsing through every symbol in fileA
        for word in symbols:
            #removing trailing and leading whitespace in symbols
            w = word.strip()
            #Searching for groupA and exchanges B and C in file B
            if "exchangeC_groupA" in line or "exchangeB_groupA" in line:
                #removing trailing and leading whitespace
                l = line.strip()
			    #extracting the symbols part of the line
                fl = l[l.find('='):]
                if w not in fl:
				    #appending the symbols to the output list
                    output.append(w)

#printing the output that is not unique (since that implies that the symbol is not found in both the cases)
print [item for item, count in collections.Counter(output).items() if count > 1]
             