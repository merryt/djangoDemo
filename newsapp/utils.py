def finds_item_in_array_based_on_keyvalue(array, key, value_to_match):
    object_to_return = None 
    for item in array:
        if item[key] == value_to_match:
            object_to_return = item
            break
        
    return object_to_return