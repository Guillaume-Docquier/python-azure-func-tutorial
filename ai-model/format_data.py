import json
import os

from myazfunc.predict import INPUT_SIZE, OUTPUT_SIZE

DATA_FOLDER = "./data/"
RAW_DATA_FOLDER = DATA_FOLDER + "raw/"

(_, _, file_names) = next(os.walk(RAW_DATA_FOLDER))

# Extract
resource_costs = []
processed = 0
nb_files = len(file_names)
for file_name in file_names[:500]:
    with open(RAW_DATA_FOLDER + file_name) as json_file:
        resources = json.load(json_file)
        # Transform
        for resource_name in resources:
            resource = resources[resource_name]
            costs = resource.values()
            # Only add resources that have enough costs
            if len(costs) >= INPUT_SIZE + OUTPUT_SIZE and any(cost > 0 for cost in costs):
                resource_costs.append(list(costs))
    processed += 1
    print(f"{processed} of {nb_files}")

print(f"{len(resource_costs)} resources to save")

# Load
nb_train_resource_costs = int(len(resource_costs) * 0.8)
with open(DATA_FOLDER + "train.json", 'w') as outfile:
    json.dump(resource_costs[:5000], outfile)

with open(DATA_FOLDER + "test.json", 'w') as outfile:
    json.dump(resource_costs[5000:7000], outfile, )
