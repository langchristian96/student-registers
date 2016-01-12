
import unittest
from Domain.Students import *


class Test(unittest.TestCase):
    def setUp(self):
        
        self.s=Student(1,'mark')
        self.s2=Student(2,'ana')
        
    def testGet(self):
        self.assertEqual(self.s.getId(), 1)
        self.assertEqual(self.s2.getId(), 2)
        self.assertEqual(self.s.getName(), 'mark')
        self.assertEqual(self.s2.getName(), 'ana')
    def testSet(self):
        self.s.setId(3)
        self.assertEqual(self.s.getId(), 3)
        self.s2.setId(4)
        self.assertEqual(self.s2.getId(), 4)
        self.s.setName('markk')
        self.assertEqual(self.s.getName(), 'markk')
        self.s2.setName('anaa')
        self.assertEqual(self.s2.getName(), 'anaa')


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()