'''
Created on 5 dec. 2015

@author: LenovoM
'''
import unittest
from Base.GradeBase import *
from Domain.Grades import * 

class Test(unittest.TestCase):


    def setUp(self):
        self.gradebase=GradeBase()
        c1=Grade('Algebra',800,'arthur',9)
        self.gradebase.add(c1)
        c2=Grade('FPcurs',50,'qwer',8)
        self.gradebase.add(c2)
        
    def testAdd(self):
        c3=Grade('Algebra',100,'qwert',10)
        c4=Grade('Algebra',100,'qasdasdwq',9)
        self.gradebase.add(c3)
        self.assertEqual(len(self.gradebase),3)
        l=self.gradebase.getAll()
        self.assertEqual(l[2].getDiscipline(), 'Algebra')
        self.assertEqual(l[2].getId(), 100)
        self.assertEqual(l[2].getGrade(), 10)
        self.assertEqual(l[2].getTeacher(), 'qwert')
        self.assertRaises(StudentException,self.gradebase.add,c4)
    def testDelete(self):
        self.gradebase.remove(800,'Algebra')
        self.assertEqual(len(self.gradebase), 1)
    def testUpdate(self):
        #id grade teacher discipline
        c=Grade('FPcurs',50,'qweqeq',5)
        self.gradebase.update(50, 5, 'qweqeq', 'FPcurs')
        c2=self.gradebase.findByDisciplineAndID(50, 'FPcurs')
        self.assertEqual(c.getGrade(),c2.getGrade() )
        self.assertEqual(c.getDiscipline(), c2.getDiscipline())
        self.assertEqual(c.getTeacher(), c2.getTeacher())
        
    def testFindById(self):
        
        c1=Grade('FPcurs',50,'qwer',8)
        c2=self.gradebase.findById(50)
        self.assertEqual(c1.getDiscipline(), c2.getDiscipline())
        self.assertEqual(c1.getGrade(), c2.getGrade())
        self.assertEqual(c1.getTeacher(), c2.getTeacher())
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()