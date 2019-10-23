class Node(object):
    """Binary search node."""

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __repr__(self):

        return f'<Node data={self.data}>'

def traverse_inorder(node):
    """Prints the value of each node in order from smallest to largest."""

    if node.left != None:
        traverse_inorder(node.left)

    print(node.data)

    if node.right != None:
        traverse_inorder(node.right)
