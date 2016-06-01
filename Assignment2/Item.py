class Item:

    def __init__(self, name, description, price, availability):

        self.name = name
        self.description = description
        self.price = price
        self.availability = availability

    def __str__(self):
        return "{}, {}, {}, {}".format(self.name, self.description, self.price, self.availability)
