import argparse
import torch
import numpy as np
import pandas as pd
from  utils.utils import load_data, load_predict_data
from  utils.predict import predict
from utils.train import train
from utils.algo_action import algo


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--training',
                       default='training.csv',
                       help='input training data file name')
    parser.add_argument('--testing',
                        default='testing.csv',
                        help='input testing data file name')
    parser.add_argument('--output',
                        default='output.csv',
                        help='output file name')
    args = parser.parse_args()
    
    # load training data
    training_data = load_data(args.training)
    
    # training
    print('training...')
    train(training_data)

    # load testing data
    testing_data = load_predict_data(args.testing)
    seq = np.append(training_data[-20:], testing_data)

    # predict
    print('predict...')
    seq_predict = predict(seq)
    action = algo(seq_predict)

    # save output file
    with open(args.output, 'w') as output_file:
        for x in action:
            output_file.write(str(x)+'\n')