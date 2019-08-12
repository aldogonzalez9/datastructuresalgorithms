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

        self.list.append(self.elements[0])
        self.list.append(self.elements[1])
        self.list.append(self.elements[2])

    def tearDown(self):
        pass

    def testAppend(self):
        
        other_element = 'hotcakes'
        self.list.append(other_element)
        result = [element for element in self.list.iter()]

        self.assertSequenceEqual(result, list(self.elements) + [other_element])

    def testSize(self):
        self.assertEqual(self.list.size, 3)
    
    def testDelete(self):
        self.list.delete(self.elements[1])
        result = [element for element in self.list.iter()]

        self.assertSequenceEqual(result, (self.elements[0], self.elements[2]) )
    
    def testSearch(self):
        self.assertEqual(self.list.search(self.elements[1]), True)