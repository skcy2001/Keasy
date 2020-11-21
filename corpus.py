import glob
import os
import csv
from itertools import islice
import math
import regex as re2

# Pre-defined variables
folder_path = 'Dataset' # Folder containing the datasets
row_count = 6587830 # No. of Dialogues
rate = 2785.5153203342757 # No. of entries read per second

def char_preprocess(text):
    # Removing Punctuations
    text = re2.sub(r'[^A-Za-z. ]', '', text)
    # Convert to lower case
    text = text.lower()
    # Remove whitespaces
    text = text.replace('_','')
    # Split in sentences
    text = text.replace('.','\n')
    return text

fhand = open("corpus.txt","a+",encoding='utf-8-sig')

# Scanner function
for filename in glob.glob(os.path.join(folder_path, '*.txt')):
    
    #Opens one file at a time and reads from it
    f = open(filename,'r',encoding='utf8')
    data = f.read()
    data = data.split('\n')
    row_count = len(data)
    #Reads line by line, preprocesses it, and writes in a file
    for line in data:
        print("FILE :", filename, "| Time left : %dm%6.3fs" %(math.floor(row_count/rate/60),row_count/rate % 60), end='\r')
        row_count = row_count - 1
        line = char_preprocess(line) + "\n"
        try: fhand.write(line)
        except: continue
    
    f.close()
print("\n",end='\r')
fhand.close()
