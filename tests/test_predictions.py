import unittest
import random
import numpy as np
import matplotlib.pyplot as plt

from costprediction.predict import INPUT_SIZE, predict_costs

SHOW_GRAPH = True

random.seed(43)

BASE_COST = 5.0
MEDIUM_INCREASE = 5.0
WEEK = 7
MAXIMUM_ERROR = 1.0


class TestMyAzFunc(unittest.TestCase):
    def test_predictions(self):
        dates = np.array([])  # Todo make some fake dates, can be just numbers
        costs = np.array([])  # Todo generate some costs

        predictions = predict_costs(costs)[:-1]  # Last one has nothing to compare to
        dates = dates[INPUT_SIZE:]  # First INPUT_SIZE data points have no predictions
        costs = costs[INPUT_SIZE:]  # First INPUT_SIZE data points have no predictions

        errors = abs(costs - predictions)
        if SHOW_GRAPH:
            show_graph("test_predictions", dates, costs, predictions, errors)

        # Todo assert


def show_graph(title, dates, costs, predictions, errors):
    error_mask = errors > MAXIMUM_ERROR

    fig, ax = plt.subplots()
    ax.plot(dates, costs, label="Actual Costs", zorder=1)
    ax.plot(dates, predictions, label="Predictions", zorder=2)
    ax.fill_between(dates, predictions - MAXIMUM_ERROR, predictions + MAXIMUM_ERROR, color="bisque")
    ax.scatter(dates[error_mask], costs[error_mask], marker="*", color="red", label="Errors", zorder=3)
    ax.legend(loc="upper left")
    plt.title(title)
    plt.show()


if __name__ == "__main__":
    unittest.main()