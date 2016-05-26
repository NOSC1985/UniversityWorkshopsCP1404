def convert_item_list_to_dictionary(list_of_items):
    dictionary_of_items = {}
    for item in list_of_items:
        item_name = item[0]
        item_details = [item[1], item[2], item[3]]
        dictionary_of_items[item_name] = item_details

    return dictionary_of_items


def convert_item_dictionary_to_list(item_dictionary):
    list_of_items = []
    item_names = item_dictionary.keys()
    for item in item_names:
        item_name = [item]
        item_description = item_dictionary[item]
        current_item = [item_name + item_description]
        list_of_items = list_of_items + current_item

    return list_of_items