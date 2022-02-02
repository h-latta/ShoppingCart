
from os import name
from shopping_cart import ShoppingCart

shopping_cart = ShoppingCart()

class Customer:

    def __init__(self):
        self.name = ""
        shopping_cart

    def set_name(self):
        name = input("What's your name? ")
        self.name = name

    def welcome_clause(self):
        print(f'Welcome {self.name}, what would you like to do?')
        next_action = input('Shop for products? Clear cart? See cart? Checkout? ')
        if next_action == 'Shop for products':
            shopping_cart.product_name()
        elif next_action == 'Clear cart':
            shopping_cart.clear_cart()
        elif next_action == "See cart":
            print(shopping_cart.shopping_list)
            print(sum(shopping_cart.shopping_list_cost))
        elif next_action == "Checkout":
            print(f'Thanks for shopping! You got {shopping_cart.shopping_list} for {sum(shopping_cart.shopping_list_cost)}.')
        else:
            print("I'm not sure what that means..")

    def second_action(self):
        ending = True
        while ending == True:
            print('What else would you like to do?')
            next_action = input('Shop for products? Clear cart? See cart? Checkout? ')
            if next_action == 'Shop for products':
                shopping_cart.product_name()
            elif next_action == 'Clear cart':
                shopping_cart.clear_cart()
            elif next_action == "See cart":
                print(shopping_cart.shopping_list)
                print(sum(shopping_cart.shopping_list_cost))
            elif next_action == "Checkout":
                print(f'Thanks for shopping, {self.name}! You got {shopping_cart.shopping_list} for {sum(shopping_cart.shopping_list_cost)} dollars.')
                break
            else:
                print("I'm not sure what that means..")
