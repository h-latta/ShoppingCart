

from os import name
from product import Product

bananas = Product('Bananas', 2.50, 'Fruit')
pizza = Product('Pizza', 5.00, 'Frozen Foods')
milk = Product('Milk', 3.60, 'Dairy')
eggs = Product('Eggs', 5.00, 'Poultry')
cereal = Product('Cereal', 4.30, 'Breakfast')

class ShoppingCart:

    def __init__(self):
        self.shopping_list = []
        self.shopping_list_cost = []

    def product_name(self):
        product_list = [bananas.name, pizza.name, milk.name, eggs.name, cereal.name]
        product_select = input(f'What product would you like to add to the cart? ({product_list}) ')
        if product_select == bananas.name:
            self.shopping_list.append(bananas.name)
            self.shopping_list_cost.append(bananas.price)
        elif product_select == pizza.name:
            self.shopping_list.append(pizza.name)
            self.shopping_list_cost.append(pizza.price)
        elif product_select == milk.name:
            self.shopping_list.append(milk.name)
            self.shopping_list_cost.append(milk.price)
        elif product_select == eggs.name:
            self.shopping_list.append(eggs.name)
            self.shopping_list_cost.append(eggs.price)
        elif product_select == cereal.name:
            self.shopping_list.append(cereal.name)
            self.shopping_list_cost.append(cereal.price)
        else:
            print('That item is not in stock.')

    def clear_cart(self):
        empty_cart = input('Would you like to empty the contents of your cart? ')
        if empty_cart == 'Yes':
            self.shopping_list_cost = []
            self.shopping_list = []