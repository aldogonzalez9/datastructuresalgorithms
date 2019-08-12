from datastructuresalgorithms.nodes.node import Node

class SinglyLinkedList:
    def __init__(self):
        self.tail = None #first node
        self.head = None #last node
        self.size = 0 #O(1)

    def append(self, data): #O(1)
        node = Node(data)
        self.size += 1
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.tail = node
            self.head = node
    
