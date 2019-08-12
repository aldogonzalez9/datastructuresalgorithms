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

        result = []
        for element in self.list.iter():
            result.append(element)
        self.assertSequenceEqual(result, elements)

    def testSize(self):
        self.list.append('some element')
        self.list.append('some other element')

        self.assertEqual(self.list.size, 2)