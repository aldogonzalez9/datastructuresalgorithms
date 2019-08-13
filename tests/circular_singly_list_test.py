from datastructuresalgorithms.lists.circular_sinlgy_linked_list import CircularSinglyLinkedList
from unittest import TestCase

class CircularSinglyLinkedListTest(TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.list = CircularSinglyLinkedList()
        self.elements = ('egg', 'ham', 'spam')

        self.list.append(self.elements[0])
        self.list.append(self.elements[1])
        self.list.append(self.elements[2])

    def tearDown(self):
        pass

    def testAppend(self): 
        other_element = 'hotcakes'
        self.list.append(other_element)
        appended_element = None
        counter = 0
        for element in self.list.iter():
            counter+=1
            if element == other_element:
                appended_element = element
                break
            elif counter > 20:
                break
        self.assertIs(other_element, appended_element)

    def testSize(self):
        self.assertEqual(self.list.size, 3)

    def testSizeAfterAppend(self):
        other_element = 'hotcakes'
        self.list.append(other_element)

        self.assertEqual(self.list.size, len(self.elements) + 1)

    def testDelete(self):
        self.list.delete(self.elements[1])
        found_element = None
        counter = 0
        for element in self.list.iter():
            counter+=1
            if element == self.elements[1]:
                found_element = element
                break
            elif counter > 20:
                break

        self.assertIsNone(found_element)

    def testSizeAfterDelete(self):
        self.list.delete(self.elements[1])

        self.assertEqual(self.list.size, len(self.elements) - 1)

    def testSizeAfterNotDelete(self):
        self.list.delete('fries')

        self.assertEqual(self.list.size, len(self.elements))

    # def testSearch(self):
    #     self.assertEqual(self.list.contain(self.elements[1]), True)

    # def testSearchNotInList(self):
    #     self.assertEqual(self.list.contain('Fries'), False)

    # def testClear(self):
    #     self.list.clear()
    #     result = [element for element in self.list.iter()]

    #     self.assertSequenceEqual(result, [])