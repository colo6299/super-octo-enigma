
def rotate_right(array, delta):
    for _ in range(delta%len(array)):
        last_item = array[-1]
        for index in range(len(array)-1, -1, -1):
            if index > 0:
                array[index] = array[index-1]
            else:
                array[index] = last_item

