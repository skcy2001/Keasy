import nltk
import pickle
import os


filename = 'corpus.txt'
try: 
    f = open(filename,'r')
except:
    print("Creating CORPUS:")
    import corpus
    f = open(filename,'r')
    print("CORPUS loaded")
lines = f.readlines(1000)

def in_dictlist(my_tuple, my_dictlist):
    for i in range(len(my_dictlist)):
        if my_dictlist[i][my_tuple[0]] == my_tuple[1]:
            return i
    return -1

def dictlistprint(model):
    for line in model:
        print(line['prompt'],':')
        for x in line['predict']:
            print(" --",x[0],"==","%5.3f" %(x[1]))

ngrams = {}
#Creating Ngrams of size 1-4 and storing their frequency
for line in lines:
    words_tokens = nltk.word_tokenize(line)
    for words in range(2,5):    
        for i in range(len(words_tokens)-words):
            seq = ' '.join(words_tokens[i:i+words])
            if  seq not in ngrams.keys():
                ngrams[seq] = 0
            ngrams[seq] = ngrams[seq] + 1
print("NGRAMS created")

model = []
# splitting the n-grams in n-1grams and the predicted word
for key in ngrams:
    text = key.rsplit(' ',1)
    freq = ngrams[key]
    pos = in_dictlist(('prompt',text[0]),model)
    if pos == -1:
        model.append({'prompt': text[0],'predict':[[text[1],freq]]})
    else: 
        model[pos]['predict'].append([text[1],freq])

print("DICT created")
# storing the likeliness of the occurence of a word and sorting the model
for line in model:
    total = sum(x[1] for x in line['predict'])
    for word in line['predict']:
        word[1] = word[1]/total
    line['predict'] = sorted(line['predict'], key = lambda x: x[1],reverse = True)
print("MODEL completed")

# Saving the model variable with pickle
with open("model.pickle", 'wb') as f:
    pickle.dump(model, f)
os.remove("corpus.txt")

