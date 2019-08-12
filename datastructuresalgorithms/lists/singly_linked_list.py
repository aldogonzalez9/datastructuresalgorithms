from datastructuresalgorithms.nodes.node import Node

class SinglyLinkedList:
    def __init__(self):
        self.tail = None #first node
        self.head = None #last node

    def append(self, data):
        #Encapusulate the data in a node
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
