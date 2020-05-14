
"""
1) Restate the Problem
    So I'm supposed to return true when the array has at least two
    of the same element inside of it?

2) Ask Clarifying Questions
    Is the list always sorted? What datatypes are expected? 

3) State Assumptions
    I'm going to assume the I'm given a list of integers in 
    arbitrary order, with some unknown number of duplicates.

4) Think Out Loud:

    4a: Brainstorm Solutions
        The naive solution to this would just be to search through the list
        once for each element, an n^2 runtime. We can beat this easily with 
        the use of a dictionary to accelerate the process. This process can
        be done with ~2n operations, with early exit, if done correctly.

    4b: Explain Your Rationale
        I think the added space of a dictionary is a good trade for the added
        benefit of being able to do this function with 2n steps. By structuring
        the function carefully, we can leave early with our answer, making our 
        best case O(1)

    4c: Discuss Tradeoffs
        The biggest tradeoff is the additional memory needed by the hash table.
        I believe this is worth the extra speed.

    4d: Suggest Improvements
        This function can be improved in several ways, most notably by using a set
        instead of a dictionary. The dictionary takes up more memory, with no 
        additional benefit in our case.


"""


def contains_duplicate(array):
    reference_dictionary = {}
    for item in array:
        if item in reference_dictionary:
            return True
        else:
            reference_dictionary[item] = True
    return False

