import json

import azure.functions as func
from .predict import predict_costs


def main(req: func.HttpRequest) -> func.HttpResponse:
    costs = req.get_json().get("costs")
    predictions = predict_costs(costs)
    response = json.dumps({"predictions": predictions})

    return func.HttpResponse(response)
