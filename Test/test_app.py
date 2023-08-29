import unittest
from App.multi import multiplicacion
class testmulti(unittest.TestCase):
    def test_multi(self):
        self.assertEqual(multiplicacion(2,3))



if __name__=="__main__":
    unittest.main()

