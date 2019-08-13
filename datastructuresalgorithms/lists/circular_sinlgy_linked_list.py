from datastructuresalgorithms.lists.singly_linked_list import SinglyLinkedList
from datastructuresalgorithms.nodes.node import Node

class CircularSinglyLinkedList(SinglyLinkedList):
    
    def append(self, data):
        node = Node(data)
        if self.head:
            self.head.next = node
            self.head = node
        else:
            self.head = node
            self.tail = node
        self.head.next = self.tail
        self.size += 1

    def delete(self, data):
        current = self.tail
        prev = self.tail
        while prev == current or prev != self.head:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                    self.head.next = self.tail
                else:
                    prev.next = current.next
                self.size -= 1
                return
            prev = current
            current = current.next

    def search(self, data):
        count = 0
        for node in self.iter():
            if data == node:
                return True
            count += 1
            if count > self.size:
                break
        return False