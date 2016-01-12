from Domain.Students import Student
from Domain.Disciplines import Discipline
from Domain.Grades import Grade
from Domain.GradeValidator import *
from Domain.StudentValidator import *
from Domain.Exceptions import StudentException
from Controller.DisciplineController import *
from Controller.StatisticsControllers import *

import operator

class UI:
    def __init__(self,gradeController,studentController,disciplineController,undoCtrl,StatisticsController):
        self.__gc=gradeController
        self.__sc=studentController
        self.__dsc=disciplineController
        self.__undoCtrl=undoCtrl
        self.__StatisticsController=StatisticsController
    @staticmethod    
    def printmenu():
        str = '\nAvailable commands:\n'
        str += '\t 1 - Add student \n'
        str += '\t 2 - Remove student \n'
        str += '\t 3 - Update Student \n'
        str += '\t 4 - Add grade \n'
        str += '\t 5 - Remove grade \n'
        str += '\t 6 - Update grade \n'
        str += '\t 7 - Show all students \n'
        str += '\t 8 - Show all grades \n'
        str += '\t 9 - Search for a student by ID \n'
        str += '\t 10 - Find grades by discipline \n'
        str += '\t 11 - Sort the list of students and grades alphabetically \n'
        str += '\t 12 - First 20% of students according to the average grade \n'
        str += '\t 13 - Undo \n'
        str += '\t 14 - Redo \n'
        
        str+= '\t 0 - Exit'
        print(str)
        
    @staticmethod
    def validInputCommand(command):
        '''
         Verifies if the given command is a valid one.
         Input: command - the given command - a string
         Output: True - if the command id valid
         False - otherwise
         Exceptions: -
         '''
        availableCommands = ['1', '2', '3', '4', '5', '6','7','8','9','10','11','12','13','14','0'];
        return (command in availableCommands)

    

    def readDiscipline(self,msg):
        '''
         Reads a discipline
         Input: msg - the message to be shown to the user before reading.
         Exceptions: -
         Output: A positive integer
        '''
        
            
        
        while True:
            try:
                res = input(msg)
                if self.__StatisticsController.getDisciplines(res)==0:
                    raise ValueError()
                break
            except ValueError:
                print("The string you introduced is not a good discipline.")
        return res
    @staticmethod
    def readPositiveInteger(msg):
        '''
         Reads a positive integer
         Input: msg - the message to be shown to the user before reading.
         Exceptions: -
         Output: A positive integer
        '''
        res = 0
        while True:
            try:
                res = int(input(msg))
                if res < 0:
                    raise ValueError()
                break
            except ValueError:
                print("The value you introduced was NOT a positive integer.")
        return res
    
    def __addStudentMenu(self):
        '''
         Adds a student to the registers.
         Input: -
         Output: a new student is read and added (if there is no other
        student with the same id).
        '''
        id=UI.readPositiveInteger("Please enter the ID(Positive number)")
        name=input("Please enter the student name")
        try:

            stud=Student(id,name)
            st=StudentValidator
            st.validate(stud)
            self.__sc.addStudent(stud)
        except StudentException as e:
            print(e)
            
    def __addGradeMenu(self):
        '''
         Adds a grade to the registers.
         Input: -
         Output: a new grade is read and added (if there is no other
        grade with the same id).
        '''
        id=UI.readPositiveInteger("Please enter the ID(Positive number)")
        discipline=self.readDiscipline("Please enter a discipline")
        teacher=input("Please enter the teacher")
        grade=UI.readPositiveInteger("Please enter the grade")
        if self.__sc.findById(id)!=None:
            try:

                gr=gradeValidator

                grd=Grade(discipline,id,teacher,grade)
                gr.validate(grd)
                self.__gc.addGrade(grd)
            except StudentException as e:
                print(e)
        else:
            print("The Student with the given id does not exist")
            
    def __removeGradeMenu(self):
        '''
         Removes a grade from the registers.
         Input: -
         Output: the grade is removed, if it exists.
        '''
        id=UI.readPositiveInteger("Please enter the ID(Positive number)")
        discipline=self.readDiscipline("Please enter a discipline")
        try:
            self.__gc.removeStudent(id,discipline)
        except StudentException as e:
            print(e)
    def __removeStudentMenu(self):
        '''
         Removes a student from the registers.
         Input: -
         Output: the student is removed, if it exists.
        '''
        id=UI.readPositiveInteger("Please enter the ID(Positive number)")
        
        try:
            self.__sc.removeStudent(id)
        except StudentException as e:
            print(e)
    def __updateStudentMenu(self):
        '''
        Updates a student from the registers.
        Input:-
        Output: the student is updated if it exists
        '''
        id=UI.readPositiveInteger("Please enter the ID(Positive number)")
        name=input("Please enter the student name")
        try:
            stud=Student(id,name)
            st=StudentValidator
            st.validate(stud)
            self.__sc.updateStudent(id,name)
        except StudentException as e:
            print(e)
    def __updateGradeMenu(self):
        '''
        Updates a grade from the registers.
        Input:-
        Output: the grade is updated if it exists
        '''
        id=UI.readPositiveInteger("Please enter the ID(Positive number)")
        discipline=self.readDiscipline("Please enter the discipline")
        teacher=input("Please enter the teacher")
        grade=UI.readPositiveInteger("Please enter the grade")
        try:
            grd=Grade(discipline,id,teacher,grade)
            gr=gradeValidator
            gr.validate(grd)
            self.__gc.updateStudent(id,grade,teacher,discipline)
        except StudentException as e:
            print(e)
    def __showAllStudentMenu(self):
        '''
        Shows all the students
        Input:-
        Output:Prints the students list
        '''
        studs=self.__sc.getAll()
        if len(studs)==0:
            print("There are no students in the registers")
        for e in studs:
            print(e)
    def __showAllGradeMenu(self):
        '''
        Shows all the grades
        Input:-
        Output:Prints the grades list
        '''
        studs=self.__gc.getAll()
        if len(studs)==0:
            print("There are no grades in the registers")
        for e in studs:
            print(e)
    def __searchStudentMenu(self):
        '''
        Searches for a student
        Input:-
        Output:Prints the student's info
        '''
        id=UI.readPositiveInteger("Please enter the ID(Positive number)")
        try:
            stud=self.__sc.findById(id)
            print(stud)
        except StudentException as e:
            print(e)
            
    def __findByDisciplineMenu(self):
        '''
        Searches for grades at a certain discipline
        Input:-
        Output:Prints the grades 
        '''
        discipline=self.readDiscipline("Please enter the discipline")
        res=self.__gc.findByDiscipline(discipline)
        if res==[]:
            print("There are no grades at the given discipline")
        else:
            for e in res:
                print(e)
    def __listOfGradesAlphabetically(self):
        '''
        Prints the grades ordered alphabetically at a certain discipline
        Input:-
        Output: Prints the grades ordered alphabetically
        '''
        discipline=self.readDiscipline("Please enter the discipline")
        res=self.__gc.findByDiscipline(discipline)
        allNames=self.__sc.getAll()
        name=[]
        
        name=self.__StatisticsController.getListGradesAlphabetically(res)
        if name==0: 
            print("there are no grades at the given discipline")
        else:
            for e in name:
                print(e.getName()," ",e.getDiscipline()," ",e.getGrade()," ",e.getTeacher())


          
    def __undoMenu(self):
        """
        Undos the previous operation.
        Input: -
        Output: prints "Undo succesfully made" if it succeeded and "Cannot undo." otherwise
        """
        res=self.__undoCtrl.undo()
        if res==True:
            print("Undo succesfully made.")
        else:
            print("Cannot undo.")
    def __redoMenu(self):
        
        """
        Redos the previous action.
        Input:-
        Output: prints "Redo succesfully made" if it succeeded and "Cannot redo." otherwise
        """
        res=self.__undoCtrl.redo()
        if res==True:
            print("Redo succesfully made")
        else:
            print("Cannot redo.")
    def __averageGradesMenu(self):
        '''
        Computes a top list of students ordered by their average grade
        Input:-
        Output:Prints the top list of students
        '''
        
        name=self.__StatisticsController.getAverageGrades()

        for e in name:

            print("Student's name: ",e['name']," Average Grade: ",e['average'])
            
    def mainMenu(self):
        commandDict = {'1': self.__addStudentMenu,
                       '2': self.__removeStudentMenu,
                       '3': self.__updateStudentMenu,
                       '4': self.__addGradeMenu,
                       '5': self.__removeGradeMenu,
                       '6': self.__updateGradeMenu,
                       '7': self.__showAllStudentMenu,
                       '8': self.__showAllGradeMenu,
                       '9': self.__searchStudentMenu,
                       '10': self.__findByDisciplineMenu,
                       '11': self.__listOfGradesAlphabetically,
                       '12': self.__averageGradesMenu,
                       '13': self.__undoMenu,
                       '14': self.__redoMenu
                       
                       
                       }
        while True:
            UI.printmenu()
            command = input("Please enter your command: ")
            while not UI.validInputCommand(command):
                print("Please enter a valid command!")
                command = input("Please enter your command: ")
            if command == '0':
                return
            commandDict[command]()

