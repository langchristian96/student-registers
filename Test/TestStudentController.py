'''
Created on 12 dec. 2015

@author: LenovoM
'''
from Domain.Disciplines import *
from Domain.Students import *
from Base.StudentBase import *
from Controller.StudentController import *
from Controller.UndoController import *
import unittest


class Test(unittest.TestCase):


    def setUp(self):
        repo=StudentBase()
        undo=UndoController()
        self.ctrl=StudentController(repo,undo)
    def testAdd(self):
        self.assertEqual(len(self.ctrl.getAll()), 0)
        s=Student(1,'mark')
        self.ctrl.addStudent(s)
        self.assertEqual(len(self.ctrl.getAll()), 1)
        l=self.ctrl.getAll()
        self.assertEqual(l[0].getId(), 1)
        self.assertEqual(l[0].getName(), 'mark')
    def testFindById(self):
        self.assertEqual(len(self.ctrl.getAll()), 0)
        s=Student(1,'mark')
        self.ctrl.addStudent(s)
        s2=self.ctrl.findById(1)
        self.assertEqual(len(self.ctrl.getAll()), 1)
        l=self.ctrl.getAll()
        self.assertEqual(s.getId(), s2.getId())
        self.assertEqual(s.getName(), s2.getName())
    def testRemove(self):
        self.assertEqual(len(self.ctrl.getAll()), 0)
        s=Student(1,'mark')
        self.ctrl.addStudent(s)
        self.assertEqual(len(self.ctrl.getAll()), 1)
        l=self.ctrl.getAll()
        self.assertEqual(l[0].getId(), 1)
        self.assertEqual(l[0].getName(), 'mark')
        s2=Student(2,'ana')
        self.ctrl.addStudent(s2)
        self.assertEqual(len(self.ctrl.getAll()), 2)
        self.ctrl.removeStudent(2)
        l=self.ctrl.getAll()
        self.assertEqual(l[0].getId(), 1)
        self.assertEqual(l[0].getName(), 'mark')
    
    def testUpdate(self):
        
        self.assertEqual(len(self.ctrl.getAll()), 0)
        s=Student(1,'mark')
        self.ctrl.addStudent(s)
        self.assertEqual(len(self.ctrl.getAll()), 1)
        l=self.ctrl.getAll()
        self.assertEqual(l[0].getId(), 1)
        self.assertEqual(l[0].getName(), 'mark')
        self.ctrl.updateStudent(1, 'markk')
        l=self.ctrl.getAll()
        self.assertEqual(l[0].getId(), 1)
        self.assertEqual(l[0].getName(), 'markk')
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()