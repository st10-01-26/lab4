# TODO решите задачу
import json


FILENAME = "input.json"


def task() -> float:
    with open(FILENAME) as file:
        python_obj = json.load(file)

    list_of_products = [d["score"] * d["weight"] for d in python_obj]
    return round(sum(list_of_products), 3)

print(task())
