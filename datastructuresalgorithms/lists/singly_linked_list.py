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
    
    def iter(self):
        current =self.tail
        while current:
            val = current.data
            current = current.next
            yield val
    
    def delete(self, data): #O(n)
        current = self.tail
        prev = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next
    
    def search(self, data):
        for node in self.iter():
            if data == node:
                return True
        return False