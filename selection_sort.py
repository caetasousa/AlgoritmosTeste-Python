from unittest import TestCase
import unittest

class SelectionSort:
    
    def ordena_array(self, array):
        for i in range(len(array)):
            for c in range(len(array) ):
                if array[i] < array[c]:
                    temp1 = array[i]
                    temp2 = array[c]

                    array[i] = temp2
                    array[c] = temp1
        return array


class TestSelectionSort(TestCase):

    def setUp(self):
        self.array = [1,7,3,2,9,0,5]
        self.objeto = SelectionSort()

        
    def test_ordena_array(self):

        self.assertListEqual([0,1,2,3,5,7,9], self.objeto.ordena_array(self.array))

if __name__ == '__main__':
    unittest.main()