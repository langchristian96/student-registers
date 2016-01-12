from __future__ import division
from Base.GradeBase import *
from Controller.ChangeHistory import *
from Controller.UndoController import *
from SortFilter import *


class GradeController:
    def __init__(self,grdBase,undoController):
        '''
         Creates a new instance of GradeController.
        '''
        self.__base=grdBase
        self.__undoController=undoController
        self.__operations=[]
        self.__index=0
        
    def addGrade(self,grd):
        '''
         Adds a grade to the registers.
         Input: grd - of type Grade
         Output: the grade is added, if there in no other grade with the
        given id
         Exceptions: raises StudentException if another grade with the
        same id already exists
        '''
        
        self.__operations=self.__operations[0:self.__index]
        self.__base.add(grd)
        self.__operations.append(AddOperation(grd))
        self.__index+=1
        self.__undoController.recordUpdatedController([self])
    def removeStudent(self,id,discipline):
        '''
         Removes a grade from the registers, using its id
         Input: id - integer, the id of the grade that must be removed
         Output: if such a grade exists, it is removed and returned
         Exceptions: raises StudentException if a grade with the given id
        does not exist
        '''
        
        self.__operations=self.__operations[0:self.__index]
        client=self.__base.findByDisciplineAndID(id,discipline)
        self.__base.remove(id,discipline)
        self.__operations.append(RemoveOperation(client))
        self.__index+=1
        self.__undoController.recordUpdatedController([self])
        
    def getAll(self):
        '''
         Returns the list of grades
        '''
        return self.__base.getAll()
    def updateStudent(self,id,newGrade,newTeacher,newDiscipline):
        '''
        Updates a grade from the registers, using its id
        Input:id-integer positive
              newGrade-integer between 0 and 10
              newTeacher-string
              newDiscipline-string
        Output:if such a grade exists, it is updated
        Exceptions: raises StudentException if a grade with the given id
        does not exist
              
        '''
        
        self.__operations=self.__operations[0:self.__index]
        oldCl=self.__base.findById(id)
        oldClient=Grade(oldCl.getDiscipline(),oldCl.getId(),oldCl.getTeacher(),oldCl.getGrade())
        
        self.__base.update(id,newGrade,newTeacher,newDiscipline)
        newCl=self.__base.findById(id)
        newClient=Grade(newCl.getDiscipline(),newCl.getId(),newCl.getTeacher(),newCl.getGrade())
        self.__operations.append(UpdateOperation(oldClient,newClient))
        self.__index+=1
        self.__undoController.recordUpdatedController([self])
    def findByDiscipline(self,discipline):
        '''
        Finds all the grades by discipline
        Input: discipline-string
        Output: result - list with all the grades at the specified discipline
        '''
        result=[]
        result=Filter(self.__base.getAll(), discipline)
        return result
    
    def averageGrade(self,id):
        '''
        Computes the average grade for the given student id
        Input: ID - integer(positive)
        Output: the average grade for the given student
        '''
        result=0
        number=0
        for m in self.__base.getAll():
            if id==m.getId():
                result+=m.getGrade()
                number+=1
        if number!=0:        
            result=result/number
        return result
    
    def undo(self):
        
        """
        Undo function for the GradeController
        """
        if self.__index==0:
            return False
        self.__index-=1
        operation=self.__operations[self.__index]
        if isinstance(operation, AddOperation):
            self.__base.remove(operation.getObject().getId(),operation.getObject().getDiscipline())
        elif isinstance(operation, RemoveOperation):
            self.__base.add(operation.getObject())
        else:
            self.__base.update(operation.getOldObject().getId(),operation.getOldObject().getGrade(),operation.getOldObject().getTeacher(),operation.getOldObject().getDiscipline())
    def redo(self):
        """
        Redo function for GradeController
        """
        if self.__index==len(self.__operations):
            return False
        
        operation=self.__operations[self.__index]
        if isinstance(operation,AddOperation):
            self.__base.add(operation.getObject())
        elif isinstance(operation, RemoveOperation):
            self.__base.remove(operation.getObject().getId(),operation.getObject().getDiscipline())
        else:
            self.__base.update(operation.getUpdatedObject().getId(),operation.getUpdatedObject().getGrade(),operation.getUpdatedObject().getTeacher(),operation.getUpdatedObject().getDiscipline())
        self.__index+=1
        
            
        
        