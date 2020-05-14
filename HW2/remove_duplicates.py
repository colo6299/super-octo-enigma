"""
1) Restate the Problem
    So what I'm trying to do is move all unique elements in the list
    to the front, in order, without worrying about duplicates or
    shortening the list?


2) Ask Clarifying Questions
    What datatypes can be expected in the array? 
    Is there a maximum or minimum length?
    What if the array is empty?

3) State Assumptions
    I'm assuming I'm going to recieve a sorted array of integers of non-zero length.


4) Think Out Loud:

    4a: Brainstorm Solutions
        The first thing that jumps out to me is making a dictionary of each number I run across, 
        but that's actually totally unneccesary. I think with a front and back pointer I can slide along 
        and "compress" the list to the left instead.

    4b: Explain Your Rationale
        Since elements are only ever removed, the elements in the array always move left. That means I can assemble 
        the array in order, in place by looking for the next unique element in the array, and placing it after the 
        last one I placed. 

    4c: Discuss Tradeoffs
        This method is a very clean in-place solution, running with O(n) operations. These are the best cases for this problem,
        as the minimum operations is n. There are other, potentially faster methods involving dictionaries that could be a
        constant time faster, but take much more memory.

    4d: Suggest Improvements
        This could be improved by cleaning up the implimentation of the exit conditions, to lower the number
        of comparisons needed for the execution of the function.

"""

def remove_duplicates_sorted(array):
    lower_index = 0
    upper_index = 1
    while upper_index < len(array):
        while array[upper_index] == array[lower_index]:
            upper_index += 1
            if upper_index == len(array):
                return lower_index + 1
        lower_index += 1
        array[lower_index] = array[upper_index]
    return lower_index + 1