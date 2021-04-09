import torch
import torch.nn as nn
from  utils.model import LSTM
import numpy as np


def normalize(data):
    '''
    x_norm = (x-xmin)/(xmax-xmin)
    '''
    data_norm = data.copy()
    data_norm = (data_norm - data.min())/(data.max()-data.min())
    data_norm = 2*data_norm - 1

    return data_norm, data.max(), data.min()


def inverse_normalize(data, data_max, data_min):
    data = (data+1)/2*(data_max-data_min)+ data_min   

    return data


def create_inout_sequences(input_data, tw):
    inout_seq = []
    L = len(input_data)
    for i in range(L-tw):
        train_seq = input_data[i:i+tw]
        train_label = input_data[i+tw:i+tw+1]
        inout_seq.append((train_seq ,train_label))
    return inout_seq


def preprocessing(training_data, train_window = 20):
    train_norm, _, _ = normalize(training_data)
    train_norm = torch.FloatTensor(train_norm).view(-1)
    train_inout_seq = create_inout_sequences(train_norm, train_window)

    return train_inout_seq


def train(training_data, epochs=5):
    # gpu or cpu
    if torch.cuda.is_available(): device = torch.device("cuda")
    else: device = torch.device("cpu")

    # preprocessing
    train_inout_seq = preprocessing(training_data)

    # train
    model = LSTM().to(device)
    loss_function = nn.MSELoss().to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

    for i in range(epochs):
        for seq, labels in train_inout_seq:
            seq, labels = seq.to(device), labels.to(device)
            optimizer.zero_grad()
            model.hidden_cell = (torch.zeros(1, 1, model.hidden_layer_size).to(device),
                            torch.zeros(1, 1, model.hidden_layer_size).to(device))
            y_pred = model(seq)
            single_loss = loss_function(y_pred, labels)
            single_loss.backward()
            optimizer.step()

        if i%10 == 1:
            print(f'epoch: {i:3} loss: {single_loss.item():10.8f}')
    print(f'epoch: {i:3} loss: {single_loss.item():10.10f}')

    # save model
    torch.save(model.state_dict(), './model')