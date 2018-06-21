"""
Created on Fri Jun 15 10:52:08 2018

@author: Matheus Schaly
"""


from abc import ABC


# Component
class Pizza(ABC):
    
    description = ""
    cost = 0

    
# Concrete Component
class Plain_Pizza(Pizza):
    
    @property
    def description(self):
        return "Thin dough"
    
    @property
    def cost(self):
        print("Cost of Dough: 4.00")
        return 4.00

    
# Decorator
class Topping_Decorator(Pizza):
    
    temp_pizza = Pizza()
    
    def __init__(self, new_pizza):
        self.temp_pizza = new_pizza
    
    @property
    def description(self):
        return self.temp_pizza.description()
    
    @property
    def get_cost(self):
        return self.temp_pizza.cost

    
# Concrete Decorator 1
class Mozzarella(Topping_Decorator):
    def __init__(self, new_pizza):
        super().__init__(new_pizza)
        print("Adding Dough")
        print("Adding Moz")
    
    @property
    def description(self):
        return super().temp_pizza.description + ", mozzarella"
    
    @property
    def cost(self):
        print("Cost of Moz: " + "0.50")
        return super().temp_pizza.cost + 0.50

    
# Concrete Decorator 2
class Tomato_Sauce(Topping_Decorator):
    def __init__(self, new_pizza):
        super().__init__(new_pizza)
        print("Adding Sauce")
    
    @property
    def description(self):
        return super().temp_pizza.description + ", tomato sauce"
    
    @property
    def cost(self):
        print("Cost of Sauce: " + "0.35")
        return super().temp_pizza.cost + 0.35


basic_pizza = Tomato_Sauce(Mozzarella(Plain_Pizza()))
print("Ingredients: " + basic_pizza.description)
print("Price: " + str(basic_pizza.cost))