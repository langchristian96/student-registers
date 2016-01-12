'''
Created on 5 dec. 2015

@author: LenovoM
'''
import unittest
from Base.StudentBase import *
from Domain.Students import *
class Test(unittest.TestCase):


    def setUp(self):
        self.studentbase=StudentBase()
        s1=Student(1,'Chris')
        self.studentbase.add(s1)
        s2=Student(2,'test')
        self.studentbase.add(s2)
        
    def testAdd(self):
        s3=Student(3,"qwer")
        s4=Student(3,'rtrewe')
        self.studentbase.add(s3)
        self.assertEqual(len(self.studentbase),3)
        self.assertRaises(StudentException,self.studentbase.add,s4)
    def testDelete(self):
        self.studentbase.remove(2)
        self.assertEqual(len(self.studentbase), 1)
        self.assertRaises(StudentException,self.studentbase.remove,24)
    def testUpdate(self):
        #id grade teacher discipline
        self.studentbase.update(1, 'chris2')
        c=self.studentbase.findById(1)
        self.assertEqual(c.getName(), 'chris2')
    def testFindById(self):
        
        c1=Student(1,'Chris')
        c2=self.studentbase.findById(1)
        self.assertEqual(c1.getId(), c2.getId())
        self.assertEqual(c1.getName(), c2.getName())
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()