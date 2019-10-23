class Node(object):
    """BST node class."""

    def __init__(self, data, left=None, right=None):

        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):

        return f'<Node data={self.data}>'


def find(node, value):
    """Starting at self node, search recursively for node with data that
    equals the inputted value."""

    if value == node.data:
        return node

    elif value < node.data and node.left == None:
        return 'That node is not in the tree.'

    elif value > node.data and node.right == None:
        return 'That node is not in the tree.'

    else:
        if value < node.data:
        find(node.left, value)

        else:
        find(node.right, value)
