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
import pickle
import regex as re2 
from keras.layers import Embedding

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

with open('variables.pickle', 'rb') as f:
    char_to_int,int_to_char = pickle.load(f)
model = keras.models.load_model("Trained_model")

def predict_next_26_chars(input_str):
    final_str = ""
    char_list=list(input_str)
    pattern = [char_to_int[char] for char in char_list]
    for i in range(1):
        X = numpy.reshape(pattern, (1,len(pattern)))
        prediction = model.predict(X, verbose=0)
        index = numpy.argmax(prediction)
        pattern.append(index)
        pattern = pattern[1:len(pattern)]
        print(int_to_char[index],end='')
    return final_str

input_str = "The boy la"
 
input_str = char_preprocess(input_str)
 # Use first 100 characeters from given input_str as input and generate next 200 characters.
input_str = input_str[:100]
print("Original String")
print(input_str)
print()
print("Predicted String")
print(predict_next_26_chars(input_str))