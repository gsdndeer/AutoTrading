import torch
from  utils.model import LSTM
import numpy as np
from utils.train import normalize, inverse_normalize


def predict(seq):
    # load model
    model = LSTM()
    model.load_state_dict(torch.load('./model'))
    model.eval()
    
    # normalize
    seq, seqmax, seqmin = normalize(seq)

    # predict
    seq_pre = []
    for i in range(20):
        row = seq[i:i+20]
        row_norm = torch.FloatTensor(row)
        with torch.no_grad():
            model.hidden = (torch.zeros(1, 1, model.hidden_layer_size),
                            torch.zeros(1, 1, model.hidden_layer_size)) 
            actual_predictions = inverse_normalize(np.array(model(row_norm).item()), seqmax, seqmin)
            seq_pre.append(actual_predictions) 
    
    return np.squeeze(seq_pre)