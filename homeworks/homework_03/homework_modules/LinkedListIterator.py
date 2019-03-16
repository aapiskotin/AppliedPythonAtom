class LinkedListIterator:
    def __init__(self, node):
        self.node = node
        self.child = None

    def __next__(self):
        if self.child is not None:
            self.node = self.child
        if self.node.next_node is None:
            raise StopIteration
        else:
            self.child = self.node.next_node
            return self.node

    def __iter__(self):
        return self
