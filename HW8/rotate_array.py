
def rotate_right(array, delta):
    """ 
    O(n*k%n) runtime where k is the number of steps to rotate
    
    O(1) memory
    """
    for _ in range(delta%len(array)):
        last_item = array[-1]
        for index in range(len(array)-1, -1, -1):
            if index > 0:
                array[index] = array[index-1]
            else:
                array[index] = last_item

