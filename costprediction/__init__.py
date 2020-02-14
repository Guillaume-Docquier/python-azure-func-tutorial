import json

import azure.functions as func
from .predict import predict_costs


def main(req: func.HttpRequest) -> func.HttpResponse:
    costs = []  # TODO get the costs from req.get_json()
    predictions = predict_costs(costs)
    response = ""  # TODO serialize the predictions using json.dumps()

    return func.HttpResponse(response)
