
class Node(object):
    """Binary search node."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def insert(value, node):
    """Inserts a new node in the proper location based on the inputted value.
    The node parameter is the starting node."""

    if value < node.data:
        if node.left == None:
            node.left = Node(value)
        else:
            insert(value, node.left)

    else:
        if node.right == None:
            node.right = Node(value)
        insert(value, node.right)
    return
