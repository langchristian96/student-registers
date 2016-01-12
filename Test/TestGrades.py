import unittest
from Domain.Grades import *
class testGrades(unittest.TestCase):
    def setUp(self):
        self.c=Grade('FPcurs',9,'arthur',10)
        self.c2=Grade('FPcurs',10,'arthur',9)
    def testGet(self):
        self.assertEqual(self.c.getDiscipline(), 'FPcurs')
        self.assertEqual(self.c2.getDiscipline(), 'FPcurs')
        self.assertEqual(self.c.getId(), 9)
        self.assertEqual(self.c2.getId(), 10)
        self.assertEqual(self.c.getTeacher(), 'arthur')
        self.assertEqual(self.c2.getTeacher(), 'arthur')
        self.assertEqual(self.c.getGrade(), 10)
        self.assertEqual(self.c2.getGrade(), 9)
    def testSet(self):
        self.c.setDiscipline('Algebra')
        self.assertEqual(self.c.getDiscipline(), 'Algebra')
        self.c2.setDiscipline('Algebra')
        self.assertEqual(self.c2.getDiscipline(), 'Algebra')
        self.c.setId(2)
        self.assertEqual(self.c.getId(), 2)
        self.c2.setId(3)
        self.assertEqual(self.c2.getId(), 3)
        self.c.setTeacher('art')
        self.assertEqual(self.c.getTeacher(), 'art')
        self.c2.setTeacher('arth')
        self.assertEqual(self.c2.getTeacher(), 'arth')
        self.c.setGrade(9)
        self.assertEqual(self.c.getGrade(), 9)
        self.c2.setGrade(8)
        self.assertEqual(self.c2.getGrade(), 8)
        
            
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()