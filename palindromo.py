import unittest

class Palindromo:
    def confere(self,palavra):
        if len(palavra) < 3:
            return "Não é um palindromo"

        if palavra[::-1] == palavra:
            return palavra[::-1]
        else:
            return "Não é um palindromo"

class TestaPalindromo(unittest.TestCase):

    def setUp(self):
        self.obj = Palindromo()
    

    def testConfereSeEPalindromo(self):
        self.assertEqual("arara", self.obj.confere("arara"))

    def testNaoEUmPalindromo(self):
        self.assertEqual("Não é um palindromo", self.obj.confere("casa"))

    def testPalavraMenorQueTresCaracteres(self):
        self.assertEqual("Não é um palindromo", self.obj.confere("ca"))

if __name__ == '__main__':
    unittest.main()