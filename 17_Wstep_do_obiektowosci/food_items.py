import csv
from pprint import pprint


class FoodItem:
    def __init__(self, item_id, item_name, price):
        self.id = int(item_id)
        self.name = item_name
        self.price = float(price)

    def __repr__(self):
        return f'FoodItem({self.id}, "{self.name}", {self.price})'


food_list = []

with open('foods.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        food_list.append(FoodItem(item_id=row['id'], item_name=row['name'], price=row['price']))

pprint(food_list)
