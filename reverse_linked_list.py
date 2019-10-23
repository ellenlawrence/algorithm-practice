class Node(object):
    """Linked list node."""

    def __init__(self, data):

        self.data = data
        self.next = None

    def __repr__(self):

        return f'<Node data={self.data} next={self.next}'

class LinkedList(object):
    """LinkedList."""

    def __init__(self):
    
        self.head = None

    def reverse(self):

        
        