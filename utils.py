import json

def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)