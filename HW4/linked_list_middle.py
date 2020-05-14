

def linked_list_middle(node):
    """
    Finds the middle item in a singly linked list, or two 
    middle items if it contains an even number of nodes.
    """
    length = 0
    head = node
    while node.next is not None:
        length += 1
        node = node.next
    node = head
    for _ in range((length//2) - 1):
        node = node.next
    if length % 2 is 0:
        return node, node.next
    else:
        return node