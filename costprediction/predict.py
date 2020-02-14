import tensorflow as tf
import numpy as np
import os

SCRIPT_PATH = os.path.abspath(__file__)
SCRIPT_DIR = os.path.dirname(SCRIPT_PATH)
MODEL_PATH = os.path.join(SCRIPT_DIR, "./model.h5")

MODEL = None
INPUT_SIZE = 7 * 12
OUTPUT_SIZE = 1


def _load_model():
    """
    Load the TensorFlow model if it is not loaded in the current context

    Azure functions often preserve their contexts between executions
    https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python#global-variables
    """
    global MODEL
    if MODEL is None:
        MODEL = tf.keras.models.load_model(MODEL_PATH)


def normalize(costs):
    return np.log(costs + 1)


def denormalize(costs):
    return np.exp(costs) - 1


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
    _load_model()

    normalized_costs = normalize(np.array(actual_costs))
    subsequences = make_subsequences(normalized_costs, INPUT_SIZE)
    predictions = MODEL.predict(subsequences, subsequences.shape[0])
    predictions = denormalize(predictions)

    return predictions.tolist()
