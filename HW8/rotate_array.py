"""
1: Restate the Problem


2: Ask Clarifying Questions


3: State Assumptions


4: Think Out Loud

    4a: Brainstorm Solutions

    4b: Explain Your Rationale

    4c: Discuss Tradeoffs

    4d: Suggest Improvements













"""
def rotate_right(array, delta):
    for _ in range(delta%len(array)):
        last_item = array[-1]
        for index in range(len(array)-1, -1, -1):
            if index > 0:
                array[index] = array[index-1]
            else:
                array[index] = last_item

