
# I really like the code for this one!
# Minimizes all array operations, I think
def move_zeroes(array):
    
    def find_replacement(insertion_index):
        for search_index in range(insertion_index, len(array)):
            if array[search_index] is not 0:
                return search_index

    zero_count = 0
    for number in array:
        if number == 0:
            zero_count += 1
    insertion_index = 0
    while insertion_index < (len(array) - zero_count):
        if array[insertion_index] is not 0:
            insertion_index += 1
        else:
            replace_index = find_replacement(insertion_index)
            if replace_index is None:
                return
            else:
                array[insertion_index] = array[replace_index]
                array[replace_index] = 0
                insertion_index += 1

