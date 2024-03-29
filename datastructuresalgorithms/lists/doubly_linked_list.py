from datastructuresalgorithms.nodes.node import DoublyLinkedNode as Node

class DoublyLinkedList(object):
    def __init__(self):
        self.head = None # beginner node
        self.tail = None # latest node
        self.count = 0
    
    def append(self, data):
        """ Append an item to the list. """
        # O(1)
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def iter(self):
        current =self.head
        while current:
            val = current.data
            current = current.next
            yield val
    
    def delete(self, data):
        #O(n)
        current = self.head
        node_deleted = False
        if current is None:
            node_deleted =False
        elif current.data == data:
            self.head = current.next
            self.head.prev = None
            node_deleted = True
        elif self.tail.data == data:
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
        else:
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                    break
                current = current.next
        if node_deleted:
            self.count -= 1

    def contain(self, data):
        for node_data in self.iter():
            if data == node_data:
                return True
        return False

    def clear(self):
        """ Clear the entire list. """
        self.tail = None
        self.head = None
        self.size = 0