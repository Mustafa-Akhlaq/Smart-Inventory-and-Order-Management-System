class Product:
    def __init__(self, id, name, category, price):
        self.id = id
        self.name = name
        self.category = category
        self.price = price

    def display(self):
        print("-----------------------------")
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Category: {self.category}")
        print(f"Price: {self.price}")
        print("-----------------------------")
