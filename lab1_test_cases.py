import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """tests is when list is equal to one whether or not the function raises a Value Error"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )


    def test_max_list_iter2(self):
        tlist = []
        self.assertEqual(max_list_iter(tlist),None)

    def test_max_list_iter3(self):
        tlist = [1,2,3,4,5,6]
        self.assertEqual(max_list_iter(tlist),6)

    def test_reverse_rec2(self):
        self.assertEqual(reverse_rec([1]),[1])


    def test_reverse_rec3(self):
        tlist=None
        with self.assertRaises(ValueError):
            reverse_rec(tlist)

    def test_bin_search2(self):
       tlist=None
       with self.assertRaises(ValueError):
            bin_search(0,0,3,tlist)

    def test_bin_search3(self):
        list_val =[7,9,23,5,6,7,8,3,5,7,9,4,6]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(3, 0, len(list_val)-1, list_val), 2 )
if __name__ == "__main__":
        unittest.main()

    
