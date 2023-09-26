from unittest import TestCase
import unittest

class InsertionSort():
    def ordena(self, array):
        for i in range(1, len(array)):
            inicio = i

            while inicio > 0:
                if array[inicio] < array[inicio - 1]:
                    temp1 = array[inicio]
                    temp2 = array[inicio - 1]

                    array[inicio] = temp2
                    array[inicio - 1] = temp1

                inicio -= 1

        return array

class TestInsertionSort(TestCase):
    def setUp(self):
        self.objeto = InsertionSort()
        self.array = [1,7,3,2,9,0,5,8,4,6]
    
    def testa_ordena(self):
        self.assertListEqual([0,1,2,3,4,5,6,7,8,9], self.objeto.ordena([1,7,3,2,9,0,5,8,4,6]))


if __name__ == '__main__':
    unittest.main()