#from keras.datasets import imdb
import os
import numpy as np
import pandas as pd
import warnings
from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.utils import plot_model
import tensorflow as tf
from tensorflow.keras import layers


import time
warnings.filterwarnings(action='ignore') 

class MyLayer(tf.keras.layers.Layer):
    def __init__(self):
        super(MyLayer, self).__init__()
        self.d1 = tf.keras.layers.Dense(64, activation = 'relu')
        self.d2 = tf.keras.layers.Dense(10, activation = 'softmax')

    def call(self, x):
        x = self.d1(x)
        return self.d2(x)


#(train_data,train_labels),(test_data,test_labels) = imdb.load_data(num_words=10000)
# id document  label
rat_train=pd.read_csv('C:\\CIJ\\cijGit\\k-digital_alpaedu_pythonStudy\\csv\\ratings_train.txt', sep = "\t" , encoding = "utf-8")
rat_test=pd.read_csv('C:\\CIJ\\cijGit\\k-digital_alpaedu_pythonStudy\\csv\\ratings_test.txt', sep = "\t" , encoding = "utf-8")

#훈련데이터 : 150000
#시험데이터 : 50000


#print(rat_train['document'].iloc[:-1].shape)

inputs = tf.keras.Input(shape=rat_train['document'].iloc[:-1].shape) # 입력노드 생성

# layer 생성
outputs = MyLayer()(inputs)

# Model 생성
model = tf.keras.Model(inputs=inputs, outputs=outputs, name="mnist_model")


model.summary()


from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.models import Sequential

# 모델 구성
model = Sequential()
model.add(Embedding(input_dim=vocab_size, output_dim=100, input_length=max_length))
model.add(LSTM(64))
model.add(Dense(1, activation='sigmoid'))

# 컴파일
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
