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
