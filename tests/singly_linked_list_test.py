from datastructuresalgorithms.lists.singly_linked_list import SinglyLinkedList
from unittest import TestCase

class SinglyLinkedListTest(TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.list = SinglyLinkedList()

    def tearDown(self):
        pass

    def testAppend(self):
        elements = ('egg', 'ham', 'spam')
        self.list.append(elements[0])
        self.list.append(elements[1])
        self.list.append(elements[2])

        current = self.list.tail
        result = []
        while current:
            result.append(current.data)
            current = current.next
        self.assertSequenceEqual(result, elements)
