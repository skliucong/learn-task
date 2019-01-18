# model.py
import os
from keras.models import Sequential
from keras.layers import Input, Dense, Dropout, Flatten, Activation
from keras.layers import Convolution2D, MaxPooling2D
from keras.optimizers import SGD
import tensorflow as tf

nb_class = 7


def build_model(mode):
    """Return the Keras model for training
    Keyword arguments:
    mode: model name specified in training and predicting script
    """
    model = Sequential()
    if mode == 'easy':
        # CNN part (you can repeat this part several times)
        model.add(Convolution2D(8, 3, 3, border_mode='valid', input_shape=(48, 48, 1)))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.8))

        # Fully connected part
        model.add(Flatten())
        model.add(Dense(16))
        model.add(Activation('relu'))
        model.add(Dense(nb_class))
        model.add(Activation('softmax'))
        opt = SGD(lr=0.01, decay=0.0)

    if mode == 'simple':
        model.add(Convolution2D(32, (1, 1), strides=1, padding='same', input_shape=(48, 48, 1)))
        model.add(Activation('relu'))
        model.add(Convolution2D(32, (5, 5), padding='same'))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Convolution2D(32, (3, 3), padding='same'))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Convolution2D(64, (5, 5), padding='same'))
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))

        model.add(Flatten())
        model.add(Dense(2048))
        model.add(Activation('relu'))
        model.add(Dropout(0.5))
        model.add(Dense(1024))
        model.add(Activation('relu'))
        model.add(Dropout(0.5))
        model.add(Dense(nb_class))
        model.add(Activation('softmax'))
        model.summary()
        # opt = SGD(lr=0.01, decay=0.0)

    model.compile(loss='categorical_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])
    model.summary()  # show the whole model in terminal
    return model
