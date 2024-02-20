import csv

from models.ingredient import Ingredient
from models.dish import Dish


# Req 3
class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = self.load_dishes(source_path)

    def load_dishes(self, path):
        with open(path, "r") as file:
            data = csv.DictReader(file)
            res = self.text_formatter(list(data))
            return res

    def text_formatter(self, list_dishes):
        data = dict()
        for dish in list_dishes:
            if dish["dish"] not in data:
                data[dish["dish"]] = Dish(dish["dish"], float(dish["price"]))
            data[dish["dish"]].add_ingredient_dependency(Ingredient(
                dish["ingredient"]), int(dish["recipe_amount"]))
        return data.values()
