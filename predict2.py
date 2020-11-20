from collections import Counter
import numpy as np
import nltk
import string

filename = 'corpus.txt'
f = open(filename,'r')
lines = f.readlines(1000)

ngrams = {}
#Creating Ngrams of size 1-4 and storing their frequency
for line in lines:
    words_tokens = nltk.word_tokenize(line)
    for words in range(1,4):    
        for i in range(len(words_tokens)-words):
            seq = ' '.join(words_tokens[i:i+words])
            if  seq not in ngrams.keys():
                ngrams[seq] = 0
            ngrams[seq] = ngrams[seq] + 1

print(ngrams)

