import tensorflow as tf
import numpy as np
import os

SCRIPT_PATH = os.path.abspath(__file__)
SCRIPT_DIR = os.path.dirname(SCRIPT_PATH)
MODEL_PATH = os.path.join(SCRIPT_DIR, "model/model.h5")

MODEL = None
INPUT_SIZE = 7 * 12
OUTPUT_SIZE = 1


def _load_model():
    # TODO use tf.keras.models.load_model
    return


def normalize(costs):
    # TODO
    return costs


def denormalize(costs):
    # TODO
    return costs


def make_subsequences(data, subsequence_size):
    """
    Create subsequences of subsequence_size with the array

    Example
    -------
    >>> make_subsequences(np.array([1, 2, 3, 4]), 2)
    array([
        [1, 2],
        [2, 3],
        [3, 4],
    ])
    """
    number_of_subsequences = data.shape[0] - subsequence_size + 1

    return np.array([data[index:subsequence_size+index] for index in range(number_of_subsequences)])


def predict_costs(actual_costs):
    # TODO make sure the model is loaded

    normalized_costs = np.array(costs)  # TODO use normalize()
    subsequences = np.array(costs[INPUT_SIZE:])  # TODO use make_subsequences()
    predictions = np.array([])  # TODO use MODEL.predict()
    predictions = np.array([])  # TODO use denormalize()

    return predictions.tolist()
