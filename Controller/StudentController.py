from Base.StudentBase import *
from Controller.ChangeHistory import *
from Controller.UndoController import *

class StudentController:
    def __init__(self,studBase,undoController):
        '''
         Creates a new instance of StudentController.
        '''
        self.__base=studBase
        self.__undoController=undoController
        self.__operations=[]
        self.__index=0
    def findById(self,id):
        return self.__base.findById(id)
    def addStudent(self,stud):
        '''
         Adds a student to the registers.
         Input: stud - of type Student
         Output: the student is added, if there in no other student with the
        given id
         Exceptions: raises StudentException if another student with the
        same id already exists
        '''
        self.__base.add(stud)
        self.__operations=self.__operations[0:self.__index]
        self.__operations.append(AddOperation(stud))
        self.__index+=1
        self.__undoController.recordUpdatedController([self])
        for e in self.__operations:
            print(e)
        
    def removeStudent(self,id):
        '''
         Removes a student from the registers, using its id
         Input: id - integer, the id of the student that must be removed
         Output: if such a student exists, it is removed and returned
         Exceptions: raises StudentException if a student with the given id
        does not exist
        '''
        client=self.__base.findById(id)
        
        self.__operations=self.__operations[0:self.__index]
        self.__base.remove(id)
        self.__operations.append(RemoveOperation(client))
        self.__index+=1
        self.__undoController.recordUpdatedController([self])
    def getAll(self):
        '''
         Returns the list of students
        '''
        return self.__base.getAll()
    def updateStudent(self,id,newName):
        '''
        Updates a student from the registers, using its id
        Input:id-integer positive
              newName-string
        Output:if such a student exists, it is updated
        Exceptions: raises StudentException if a grade with the given id
        does not exist
              
        '''
        
        self.__operations=self.__operations[0:self.__index]
        oldCl=self.__base.findById(id)
        oldClient=Student(oldCl.getId(),oldCl.getName())
        
        self.__base.update(id,newName)
        newCl=self.__base.findById(id)
        newClient=Student(newCl.getId(),newCl.getName())
        self.__operations.append(UpdateOperation(oldClient,newClient))
        print(oldCl.getName())
        self.__index+=1
        self.__undoController.recordUpdatedController([self])
    
    def undo(self):
        """
        Undo function for StudentController
        """
        if self.__index==0:
            return False
        self.__index-=1
        operation=self.__operations[self.__index]
        
        
        if isinstance(operation, AddOperation):
            self.__base.remove(operation.getObject().getId())
        elif isinstance(operation, RemoveOperation):
            self.__base.add(operation.getObject())
        else:
            print(operation.getOldObject().getName())
            self.__base.update(operation.getOldObject().getId(),operation.getOldObject().getName())
    def redo(self):
        """
        Redo function for StudentController
        """
        
        if self.__index==len(self.__operations):
            return False        
        
        
        operation=self.__operations[self.__index]
        if isinstance(operation,AddOperation):
            self.__base.add(operation.getObject())
        
        elif isinstance(operation, RemoveOperation):
            self.__base.remove(operation.getObject().getId())
        
        else:
        
            self.__base.update(operation.getUpdatedObject().getId(),operation.getUpdatedObject().getName())
        
        self.__index+=1
        
   
