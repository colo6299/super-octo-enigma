def contains_duplicate(array):
    reference_dictionary = {}
    for item in array:
        if item in reference_dictionary:
            return True
        else:
            reference_dictionary[item] = True
    return False

