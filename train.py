import os
import csv
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
import numpy
import re
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import keras
import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize
import heapq


# Load the data and preprocess data and store corpus in raw_text
import os
import glob
import csv
from itertools import islice

folder_path = 'Dataset'
corpus = str()
for filename in glob.glob(os.path.join(folder_path, '*.csv')):
  with open(filename, 'r',encoding='utf8') as f:
    data = csv.reader(f,delimiter = ',')
    print("FILE :" , filename)
    row_count = 16587830
    for line in islice(data,1000):
      print(row_count," out of 16587830 left",end='\r')
      row_count = row_count - 1
      try:
        corpus = corpus + " " + line[5]
      except:
        continue
      
# Preprocessing
import regex as re2  

# User the preprocess data and create raw_text
def char_preprocess(text):
    # Removing Punctuations
    text = re2.sub(r"[^\P{P},.]+", "", text)
    # Convert to lower case
    text = text.lower()
    # Remove whitespaces
    text = text.replace('_','')
    # Remove \n tags
    text = text.replace('\n','')
    return text
raw_text = char_preprocess(corpus)

# create mapping of unique characters to integers
chars = sorted(list(set(raw_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))

# Print the total characters and character vacob size
n_chars = len(raw_text)
n_vocab = len(char_to_int)
print ("Total Characters: ", n_chars)
print ("Total Vocab: ", n_vocab)

seq_length = 100
dataX = []
dataY = []
for i in range(0, n_chars - seq_length, 1):
  seq_in = raw_text[i:i + seq_length]
  seq_out = raw_text[i + seq_length]
  dataX.append([char_to_int[char] for char in seq_in])
  dataY.append(char_to_int[seq_out])
n_patterns = len(dataX)
print ("Total Patterns: ", n_patterns)

X = numpy.array(dataX)

# one hot encode the output variable
dataY = numpy.array(dataY)
y = np_utils.to_categorical(dataY)

embedding_dim =100
max_length =100

from keras.layers import Embedding

model = Sequential()
model.add(Embedding(n_vocab, embedding_dim, input_length=max_length))
model.add(LSTM(256))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()
model.fit(X, y, epochs=1, batch_size=128, validation_split=0.2)
model.save("Trained_model")

#implement mapping of integer to character
int_to_char = dict((i, c) for i, c in enumerate(chars))

def predict_next_26_chars(input_str):
  char_list=list(input_str)
  pattern = [char_to_int[char] for char in char_list]
  for i in range(26):
    X = numpy.reshape(pattern, (1,len(pattern)))
    prediction = model.predict(X, verbose=0)
    index = numpy.argmax(prediction)
    result = int_to_char[index]
    pattern.append(index)
    pattern = pattern[1:len(pattern)]
    final_str += result

  return final_str

import pickle
with open("Variables", 'wb') as f:
  pickle.dump([char_to_int,int_to_char], f)

input_str = "The boy laughed at the fright he had caused. This time, the villagers left angrily. The third day, as the boy went up\
 the small hill, he suddenly saw a wolf attacking his sheep. He cried as hard as he could, “Wolf! Wolf! Wolf!”, but not \
 a single villager came to help him. The villagers thought that he was trying to fool them again and did not come to rescue \
 him or his sheep."
 
input_str = char_preprocess(input_str)
 # Use first 100 characeters from given input_str as input and generate next 200 characters.
input_str = input_str[:100]
print("Original String")
print(input_str)
print()
print("Predicted String")
print(predict_next_100_chars(input_str,1))
