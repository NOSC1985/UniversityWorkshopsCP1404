class ItemList:

    def __init__(self, list):

        self.list = list

    def get_whole_list(self):

        return self.list

    def get_specific_item(self,item_name):
        search_name = item_name

        for item in self.list:
            if item.name == search_name:
                return item

    def add_item(self, item_to_add):
        print(len(self.list))
        print(item_to_add)
        new_list = [item_to_add]
        for item in self.list:
            new_list.append(item)
        print(len(self.list))
        self.list = new_list

    def __str__(self):
        list_to_print = []
        string_to_print = ''
        for item_in_list in self.list:
            list_to_print = list_to_print + item_in_list

        for item in list_to_print:
            string_to_print += "\n{}, {}, {}, {}".format(item.name, item.description, item.price, item.availability)

        return string_to_print
