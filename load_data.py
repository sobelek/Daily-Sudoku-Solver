import tensorflow as tf
import os
import cv2
import random
import numpy as np
import pickle
import matplotlib.pyplot as plt
DATADIR = "./training_data/"
IMG_SIZE = 30
training_data = []
def create_traing_data():
    for i in range(10):
        path = DATADIR + str(i)
        for img in os.listdir(path):
            img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
            img_resised = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
            training_data.append([img_resised, i])


create_traing_data()
random.shuffle(training_data)
X = []
Y = []
for features, labels in training_data:
    X.append(features)
    Y.append(labels)


X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
pickle_out = open("x.pickle", "wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle", "wb")
pickle.dump(Y, pickle_out)
pickle_out.close()
