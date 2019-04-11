import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")

    def test_eq(self):
        loc1 = Location("Seattle", 456, -120.7)
        loc2 = Location("Belgrade", 123, -799)
        loc3 = Location("Vancouver", 35.3, -120.7)
        loc4 = Location("Vancouver", 35.3, -120.7)
        self.assertEqual(loc1 == loc2,False)
        self.assertEqual(loc1 == loc3,False)
        self.assertEqual(loc3 == loc2,False)
        self.assertEqual(loc3 == loc4,True)

    
if __name__ == "__main__":
        unittest.main()
