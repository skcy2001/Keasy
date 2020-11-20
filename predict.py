import pickle 

def load_model():
    with open("model.pickle", 'rb') as f:
        model = pickle.load(f)
    f.close()
    return model

def in_dictlist(my_tuple, my_dictlist):
    for i in range(len(my_dictlist)):
        if my_dictlist[i][my_tuple[0]] == my_tuple[1]:
            return i
    return -1

def predict(mod,input_str,x):
    pos = in_dictlist(("prompt",input_str.lower()),mod)
    if pos == -1:
        return {}
    else: 
        prediction = []
        for i in range(x):
            try: prediction.append(mod[pos]["predict"][i][0])
            except: pass
        return prediction
