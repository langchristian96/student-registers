import unittest
from Domain.Disciplines import *
class TestDisciplines(unittest.TestCase):
    def setUp(self):
        self.discipline=Discipline('qwert')
    
    
    def testGetDiscipline(self):
        self.assertEqual(self.discipline.getDiscipline(), 'qwert')
        
    def testSetDiscipline(self):
        self.discipline.setDiscipline('qwerty')
        self.assertEqual(self.discipline.getDiscipline(), 'qwerty')
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()