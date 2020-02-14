import unittest
import random
import numpy as np
import matplotlib.pyplot as plt

from myazfunc.predict import INPUT_SIZE, predict_costs

SHOW_GRAPH = True
ADD_NOISE = False

random.seed(43)

BASE_COST = 5.0
MEDIUM_INCREASE = 5.0
WEEK = 7


class TestMyAzFunc(unittest.TestCase):
    def test_predictions(self):
        data_size = 52 * WEEK
        increase_start = 30 * WEEK
        increase_duration = 3 * WEEK

        dates = np.array(list(range(data_size)))
        costs = np.array([BASE_COST if day < increase_start else BASE_COST + min((day - increase_start) / increase_duration, 1) * MEDIUM_INCREASE for day in range(data_size)])

        predictions = predict_costs(costs)[:-1]  # Last one has nothing to compare to
        dates = dates[INPUT_SIZE:]  # First INPUT_SIZE data points have no predictions
        costs = costs[INPUT_SIZE:]  # First INPUT_SIZE data points have no predictions

        if SHOW_GRAPH:
            show_graph("test_predictions", dates, costs, predictions)


def show_graph(title, dates, costs, predictions):
    fig, ax = plt.subplots()
    ax.plot(dates, costs, label="Actual Costs", zorder=1)
    ax.plot(dates, predictions, label="Predictions", zorder=2)
    ax.legend(loc="upper left")
    plt.title(title)
    plt.show()


def noise_factor(mean=1.0, std=0.02, chance=0.1):
    roll = random.uniform(0, 1)
    if ADD_NOISE and roll < chance:
        return random.gauss(mean, std)

    return 1


if __name__ == "__main__":
    unittest.main()