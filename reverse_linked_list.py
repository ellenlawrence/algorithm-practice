[1, 2, 3, 4]

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

        prev = None
        current = self.head

        while current:

            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev
        
    def insert_at_beginning(self, data):

        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_ll(self):

        current = self.head

        while current:

            print(current.data)
            current = current.next

            
