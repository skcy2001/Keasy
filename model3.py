import nltk
import pickle
import os
from fast_autocomplete import AutoComplete
import matplotlib.pyplot as plt
from itertools import islice

filename = 'corpus.txt'
try: 
    f = open(filename,'r')
except:
    print("Creating CORPUS:")
    import corpus
    f = open(filename,'r')
    print("CORPUS loaded")

lines = f.readlines(100000000)
print("LINES READ : ",len(lines))

try: 
    f=open("count.pickle",'rb')
    count = pickle.load(f)
except:
    count = {}
    i,j,k = 0,0,0
    for line in lines:
        j =j+1
        words = line[:-1].split(' ')
        for word in words:
            i = i+1
            print("Words counted :",i,"| uwords: ",k,"| lines: ",j,end = '\r')
            if word in count:
                count[word] += 1
            else:
                count[word] = 1
                k = k+1

    with open("count.pickle", 'wb') as f:
        pickle.dump(count, f)

print("STARTED WRITING")
f2 = open("count.json","w")
f2.write("{\n")
i=0
for word in count.keys():
    i = i+1
    print("WORDS WRITTEN:",i,end='\r')
    f2.write("\t\""+word+"\":"+" [\n")
    f2.write("\t\t{},\n")
    f2.write("\t\""+word+"\",\n")
    f2.write("\t"+str(count[word])+"\n\t],\n")

f2.write("}\n")


