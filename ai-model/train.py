import tensorflow as tf
import numpy as np
import json

from costprediction.predict import INPUT_SIZE, OUTPUT_SIZE, normalize, make_subsequences

BATCH_SIZE = 128
EPOCHS = 5
VALIDATION_SPLIT = 0.15

TRAIN_DATA_PATH = "./data/train.json"


def main():
    print('Building model')
    model = build_model()

    print('Loading train data')
    x_train, y_train = get_data(TRAIN_DATA_PATH)

    print('Fitting model on training data')
    # TODO Use model.fit()

    print('\nSaving model')
    model.save("./model.h5")


def build_model():
    # Model
    model = tf.keras.models.Sequential()

    # Convolutions
    model.add(tf.keras.layers.Reshape((INPUT_SIZE, 1), input_shape=(INPUT_SIZE,)))
    model.add(tf.keras.layers.Conv1D(filters=64, kernel_size=3, activation='relu'))
    model.add(tf.keras.layers.Conv1D(filters=64, kernel_size=3, activation='relu'))
    model.add(tf.keras.layers.Conv1D(filters=32, kernel_size=3, activation='relu'))
    model.add(tf.keras.layers.Conv1D(filters=32, kernel_size=3, activation='relu'))

    # Classification
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(128, activation='relu'))

    # Output
    model.add(tf.keras.layers.Dense(OUTPUT_SIZE, activation='relu'))

    model.summary()

    model.compile(optimizer='adam', loss='mse')

    return model


def get_data(file_path):
    # TODO Get the data from file
    # TODO Normalize the data, and make the subsequences
    all_subsequences = []

    x = np.array(all_subsequences)  # TODO Get the right shape and type
    y = np.array(all_subsequences)  # TODO Get the right shape and type

    return x, y


# This is how you define a file entry point
# When the python interpreter reads a source file, it sets the special variable "__name__"
# It will be "__main__" when you call your file in the command line.
if __name__ == "__main__":
    main()
