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
        self.elements = ('egg', 'ham', 'spam')

    def tearDown(self):
        pass

    def testAppend(self):
        
        self.list.append(self.elements[0])
        self.list.append(self.elements[1])
        self.list.append(self.elements[2])

        result = []
        for element in self.list.iter():
            result.append(element)
        self.assertSequenceEqual(result, self.elements)

    def testSize(self):
        self.list.append(self.elements[0])
        self.list.append(self.elements[1])

        self.assertEqual(self.list.size, 2)
    
    def testDelete(self):
        self.list.append(self.elements[0])
        self.list.append(self.elements[1])
        self.list.append(self.elements[2])

        self.list.delete(self.elements[1])

        result = []
        for element in self.list.iter():
            result.append(element)

        self.assertSequenceEqual(result, (self.elements[0], self.elements[2]) )