from datastructuresalgorithms.lists.doubly_linked_list import DoublyLinkedList
from unittest import TestCase

class DoublyLinkedListTest(TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.list = DoublyLinkedList()
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
        self.assertEqual(self.list.count, 3)

    def testSizeAfterAppend(self):
        other_element = 'hotcakes'
        self.list.append(other_element)

        self.assertEqual(self.list.count, 4)

    def testDelete(self):
        self.list.delete(self.elements[1])
        result = [element for element in self.list.iter()]

        self.assertSequenceEqual(result, (self.elements[0], self.elements[2]) )

    def testSizeAfterDelete(self):
        self.list.delete(self.elements[1])

        self.assertEqual(self.list.count, 2)

    def testSizeAfterNotDelete(self):
        self.list.delete('fries')

        self.assertEqual(self.list.count, 3)

    def testSearch(self):
        self.assertEqual(self.list.contain(self.elements[1]), True)

    def testSearchNotInList(self):
        self.assertEqual(self.list.contain('Fries'), False)

    # def testClear(self):
    #     self.list.clear()
    #     result = [element for element in self.list.iter()]

    #     self.assertSequenceEqual(result, [])