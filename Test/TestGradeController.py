'''
Created on 12 dec. 2015

@author: LenovoM
'''
import unittest
from Domain.Grades import *
from Domain.Disciplines import *
from Base.GradeBase import *
from Controller.GradeController import *


class Test(unittest.TestCase):
    def setUp(self):
        l=UndoController()
        grd=Grade('FP',1,'arthur',10)
        repo=GradeBase()
        self.ctrl=GradeController(repo,l)
        
        
    def testAddGrade(self):
        grd=Grade('FP',1,'arthur',10)
        self.assertEqual(len(self.ctrl.getAll()), 0)
        self.ctrl.addGrade(grd)
        self.assertEqual(len(self.ctrl.getAll()), 1)
        
        e=self.ctrl.getAll()
        self.assertEqual(e[0].getId(), 1)
        self.assertEqual(e[0].getDiscipline(), 'FP')
        self.assertEqual(e[0].getTeacher(), 'arthur')
        self.assertEqual(e[0].getGrade(), 10)
    def testRemoveGrade(self):
        grd=Grade('FP',1,'arthur',10)
        self.assertEqual(len(self.ctrl.getAll()), 0)
        self.ctrl.addGrade(grd)
        self.assertEqual(len(self.ctrl.getAll()), 1)
        self.ctrl.removeStudent(1, 'FP')
        self.assertEqual(len(self.ctrl.getAll()), 0)
    

    def testUpdateGrade(self):
        grd=Grade('FP',1,'arthur',10)
        self.assertEqual(len(self.ctrl.getAll()), 0)
        self.ctrl.addGrade(grd)
        e=self.ctrl.getAll()
        self.assertEqual(e[0].getId(), 1)
        self.assertEqual(e[0].getDiscipline(), 'FP')
        self.assertEqual(e[0].getTeacher(), 'arthur')
        self.assertEqual(e[0].getGrade(), 10)
        self.ctrl.updateStudent(1, 9, 'art', 'FP')
        l=self.ctrl.getAll()
        self.assertEqual(l[0].getId(), 1)
        self.assertEqual(l[0].getDiscipline(), 'FP')
        self.assertEqual(l[0].getTeacher(), 'art')
        self.assertEqual(l[0].getGrade(), 9)
    def testAverageGrade(self):
        grd=Grade('FP',1,'arthur',10)
        self.assertEqual(len(self.ctrl.getAll()), 0)
        self.ctrl.addGrade(grd)
        grd2=Grade('FPcurs',1,'art',9)
        self.ctrl.addGrade(grd2)
        self.assertEqual(self.ctrl.averageGrade(1), 9.5)
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()