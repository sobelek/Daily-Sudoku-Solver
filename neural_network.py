import tensorflow as tf

from tensorflow._api.v1.keras.callbacks import TensorBoard
import pickle

NAME = "Number detection"
tensorboard = TensorBoard(log_dir="logs/{}".format(NAME))
pickle_in = open("x.pickle", "rb")
X = pickle.load(pickle_in)
X = X/255.0
pickle_in = open("y.pickle", "rb")
Y = pickle.load(pickle_in)

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=X.shape[1:]),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(X, Y,batch_size=20,  epochs=200, validation_split=0.1, callbacks=[tensorboard])
model.save("number_model.model")
