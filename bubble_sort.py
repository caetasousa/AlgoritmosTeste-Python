from unittest import TestCase
import unittest


class BubbleSort():

    def ordena(self, numeros):
        for f in range(len(numeros)):
            for c in range(len(numeros) - 1):
                if numeros[c] > numeros[c + 1]:
                    temp1 = numeros[c]
                    temp2 = numeros[c + 1]

                    numeros[c] = temp2
                    numeros[c + 1] = temp1
        return numeros

class TestOrdenacao(TestCase):
    
    def setUp(self):
        self.numeros = [1, 7, 3, 2, 9, 0, 5]
        self.objeto = BubbleSort()

    def testaOrdenacao(self):
        self.assertListEqual([0,1,2,3,5,7,9], self.objeto.ordena(self.numeros))

if __name__ == '__main__':
    unittest.main()